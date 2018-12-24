
from docqa.triviaqa.training_data import ExtractMultiParagraphsPerQuestion
from docqa.data_processing.preprocessed_corpus import PreprocessedData
from docqa.scripts.ablate_triviaqa import get_model
from docqa.text_preprocessor import WithIndicators
from docqa.data_processing.document_splitter import MergeParagraphs, ShallowOpenWebRanker
from docqa.data_processing.multi_paragraph_qa import StratifyParagraphSetsBuilder

mode = "shared-norm"
model = get_model(100, 140, mode, WithIndicators())
extract = ExtractMultiParagraphsPerQuestion(MergeParagraphs(400), ShallowOpenWebRanker(16), model.preprocessor, intern=True)

oversample = [1] * 2
train = StratifyParagraphSetsBuilder(30, mode == "merge", True, oversample)

data = PreprocessedData(None, extract, train, None)
data.load_preprocess("/data/disk4/private/liujiahua/data.pkl")

training_data = data.get_train().get_epoch()
outputs = []
for batch in training_data:
  last_qid = None
  current = {"question_id": "", "question": [], "context": [], "answer_spans": [], "answer_text": []}
  for instance in batch:
    if last_qid and instance.question_id != last_qid:
      outputs.append(current)
      current = {"question": [], "context": [], "answer_spans": [], "answer_text": []}
    if current["question"]:
      assert(current["question"] == instance.question)
      assert(current["answer_text"] == instance.answer.answer_text)
    else:
      current["question"] = instance.question
      current["answer_text"] = instance.answer.answer_text
      current["question_id"] = instance.question_id
    current["context"].append(instance.context)
    current["answer_spans"].append(instance.answer.answer_spans.tolist())
    last_qid = instance.question_id

outputs.append(current)
out_file = "/data/disk4/private/liujiahua/output.json"
import json
with open(out_file, "w") as fout:
  for output in outputs:
    fout.write(json.dumps(output, ensure_ascii=False) + "\n")

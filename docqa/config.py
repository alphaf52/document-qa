from os.path import join, expanduser, dirname

"""
Global config options
"""

# VEC_DIR = join(expanduser("~"), "data", "glove")
# VEC_DIR = "/data/disk1/private/liujiahua/document-qa/data/glove"
VEC_DIR = "/data/disk1/private/liujiahua/document-qa/data/sogout_skipgram"

SQUAD_SOURCE_DIR = join(expanduser("~"), "data", "squad")
SQUAD_TRAIN = join(SQUAD_SOURCE_DIR, "train-v1.1.json")
SQUAD_DEV = join(SQUAD_SOURCE_DIR, "dev-v1.1.json")

# NEW = "/data/disk1/private/liujiahua/sequence_doc"
# NEW2 = "/data/disk1/private/liujiahua/sequence_doc_without_first_paragraph"
# NEW3 = "/data/disk1/private/liujiahua/sequence_doc_without_title"

NEW_ZH = "/data/disk1/private/liujiahua/sequence_doc_zh"

# TRIVIA_QA = join(expanduser("~"), "data", "triviaqa")
TRIVIA_QA = "/data/disk1/private/liujiahua/triviaqa_sample"

TRIVIA_QA_UNFILTERED = join(expanduser("~"), "data", "triviaqa-unfiltered")
LM_DIR = join(expanduser("~"), "data", "lm")
DOCUMENT_READER_DB = join(expanduser("~"), "data", "doc-rd", "docs.db")


CORPUS_DIR = join(dirname(dirname(__file__)), "data")

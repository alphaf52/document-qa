from os.path import join, expanduser, dirname

"""
Global config options
"""

# VEC_DIR = join(expanduser("~"), "data", "glove")
VEC_DIR = "/data1/private/liujiahua/document-qa/data/glove"
# VEC_DIR = "/data/disk1/private/liujiahua/document-qa/data/sogout_skipgram"

SQUAD_SOURCE_DIR = join(expanduser("~"), "data", "squad")
SQUAD_TRAIN = join(SQUAD_SOURCE_DIR, "train-v1.1.json")
SQUAD_DEV = join(SQUAD_SOURCE_DIR, "dev-v1.1.json")

NEW_EN = "/data1/private/liujiahua/wiki_data_en"
NEW_FR_TRANS = "/data1/private/liujiahua/wiki_data_fr/translate_en"
NEW_DE_TRANS = "/data1/private/liujiahua/wiki_data_de/translate_en"
NEW_RU_TRANS = "/data1/private/liujiahua/wiki_data_ru/translate_en"
NEW_PT_TRANS = "/data1/private/liujiahua/wiki_data_pt/translate_en"
NEW_ZH_TRANS = "/data1/private/liujiahua/wiki_data_zh/translate_en"
NEW_FR_ORI = "/data1/private/liujiahua/wiki_data_fr"
NEW_DE_ORI = "/data1/private/liujiahua/wiki_data_de"
NEW_RU_ORI = "/data1/private/liujiahua/wiki_data_ru"
NEW_PT_ORI = "/data1/private/liujiahua/wiki_data_pt"
NEW_ZH_ORI = "/data1/private/liujiahua/wiki_data_zh"

CORPUS_NAME_TO_PATH = {
  "wiki_en": NEW_EN,
  "wiki_fr_trans_en": NEW_FR_TRANS,
  "wiki_de_trans_en": NEW_DE_TRANS,
  "wiki_ru_trans_en": NEW_RU_TRANS,
  "wiki_pt_trans_en": NEW_PT_TRANS,
  "wiki_zh_trans_en": NEW_ZH_TRANS,
  "wiki_fr_ori": NEW_FR_ORI,
  "wiki_de_ori": NEW_DE_ORI,
  "wiki_ru_ori": NEW_RU_ORI,
  "wiki_pt_ori": NEW_PT_ORI,
  "wiki_zh_ori": NEW_ZH_ORI,
}

# TRIVIA_QA = join(expanduser("~"), "data", "triviaqa")
TRIVIA_QA = "/data/disk1/private/liujiahua/triviaqa_sample"

TRIVIA_QA_UNFILTERED = join(expanduser("~"), "data", "triviaqa-unfiltered")
LM_DIR = join(expanduser("~"), "data", "lm")
DOCUMENT_READER_DB = join(expanduser("~"), "data", "doc-rd", "docs.db")


CORPUS_DIR = join(dirname(dirname(__file__)), "data")

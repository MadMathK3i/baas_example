# -*- coding:utf-8 -*-
from bert_serving.client import BertClient
bc_jp = BertClient()

import sentencepiece as spm
s = spm.SentencePieceProcessor()
s.Load('/home/k3ijo/bert/nlp_model/bert-jp/wiki-ja.model')

def parse(text):
    text = text.lower()
    return s.EncodeAsPieces(text)

#texts = ["BERTのテスト","覚悟はいいか？オレはできてる"]

parsed_texts = [["Are","you","ready","?","I'm","ready"]]

#parsed_texts = list(map(parse,texts))

print(bc_jp.encode(parsed_texts,is_tokenized=True))

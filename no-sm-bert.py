# -*- coding: utf-8 -*-

from bert_serving.client import BertClient
bc = BertClient()

text_list = ["お世話になります。","はじめまして、","株式会社バートアズサービスの伊藤花子と申します。"]

print(bc.encode(text_list))


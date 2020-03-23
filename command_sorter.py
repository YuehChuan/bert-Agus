# -*- coding: utf-8 -*-
from bert_serving.client import BertClient
from scipy import spatial
from numpy import argmax
from opencc import OpenCC
from comment import Comment


class Sorter:
    def __init__(self, c:Comment):
        #DTO refactor with Data transfer object  是否要繼承super,啟用init 因為Sorter算是連接物件helper
        #classmethod static method
        self.c = c

        #函式內部使用
        self.cc = OpenCC('t2s')  # 繁轉簡
        self.bc = BertClient()  # 取得bert服務器資源
        self.classes_enc = None


    def cosine_sim(self, v1, v2):
        return 1 - spatial.distance.cosine(v1, v2)

    def predict_label(self, v):
        cos_sim = []
        for i, c in enumerate(self.classes_enc):
            cos_sim.append(self.cosine_sim(v, c))
        return argmax(cos_sim)

    def predict_labels(self, vs):
        op = []
        for v in vs:
            op.append(self.predict_label(v))
        return op

    def command_sort(self,Labeles):

        sent = self.c.input_comment
        labels = self.c.ground_truth
        classes = [self.cc.convert(s) for s in Labeles] #把Label轉簡體 因為模型簡體練的

        self.classes_enc = self.bc.encode(classes)  # 把Label們轉換成數值向量
        print("True Label:", labels)
        print("Predict Label:", self.predict_labels(self.bc.encode(sent)))
        self.c.prediction = self.predict_labels(self.bc.encode(sent))
        return 0

    def single_comment_sort(self,Labeles):

        sent = self.c.input_comment
        labels = self.c.ground_truth
        classes = [self.cc.convert(s) for s in Labeles] #把Label轉簡體 因為模型簡體練的

        self.classes_enc = self.bc.encode(classes)  # 把Label們轉換成數值向量
        #print("True Label:", labels)
        print("Predict Label:", self.predict_labels(self.bc.encode(sent)))
        self.c.prediction= self.predict_labels(self.bc.encode(sent))
        result = self.c.prediction[0]
        return result

    def print_validate_result(self):

        print("True Label:", self.true_label)
        print("Predict Label:", self.result)
        return 0




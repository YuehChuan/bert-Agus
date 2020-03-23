# -*- coding: utf-8 -*-
from command_sorter import Sorter
from comment import Comment


Labels = ["外部放電", "內部放電", "雜訊干擾"]

input_comment = [
    "受DS-TIE外部放電影響。",
    "外部放電。",
    "經現場定位雷丘內部放電",
    "內部放電皮卡皮卡。",
    "受雜訊干擾。",
    "雜訊干擾。",
]

c = Comment()
c.input_comment = input_comment
c.ground_truth = [0, 0, 1, 1, 2, 2]
s = Sorter(c)
s.command_sort(Labels)

truth_labels=c.ground_truth
predicted_labels=c.prediction



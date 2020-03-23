# -*- coding: utf-8 -*-
import unittest
from command_sorter import Sorter
from comment import Comment

class TestSorter(unittest.TestCase):
    def test_command_sorter(self):
        Labels = ["外部放電", "內部放電", "雜訊干擾"]

        input_comment = [
            "受DS-TIE外部放電影響。",
            "外部放電。",
            "經現場定位雷丘內部放電",
            "內部放電皮卡皮卡。",
            "受雜訊干擾。",
            "雜訊干擾。",
        ]


        c=Comment()
        c.input_comment=input_comment
        c.ground_truth=[0, 0, 1, 1, 2, 2]
        s = Sorter(c)
        s.command_sort(Labels)

        self.assertEqual(s.c.prediction, [0, 0, 1, 1, 2, 2])
    def test_single_comment_sort(self):
        Labels = ["外部放電","內部放電", "雜訊干擾"]

        input_comment = [
            "受DS-TIE外部放電影響",
        ]

        c = Comment()  # concern memory usage
        c.input_comment = input_comment
        c.ground_truth = 0
        s = Sorter(c)
        result = s.single_comment_sort(Labels)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()

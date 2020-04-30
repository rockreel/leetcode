import unittest

import common
from l0295_find_median_from_data_stream import MedianFinder

class Test(unittest.TestCase):
    
    def test_solution(self):
        # finder =  MedianFinder()
        # finder.addNum(1)
        # finder.addNum(2)
        # self.assertEqual(1.5, finder.findMedian())
        # finder.addNum(3)
        # self.assertEqual(2, finder.findMedian())

        finder =  MedianFinder()
        finder.addNum(-1)
        finder.addNum(-2)
        self.assertEqual(-1.5, finder.findMedian())
        finder.addNum(-3)
        self.assertEqual(-2, finder.findMedian())

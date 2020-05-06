import unittest

from l0303_range_sum_query_immutable import NumArray

class Test(unittest.TestCase):
    
    def test_solution(self):
        na = NumArray([-2, 0, 3, -5, 2, -1])
        self.assertEqual(1, na.sumRange(0, 2))
        self.assertEqual(-1, na.sumRange(2, 5))
        self.assertEqual(-3, na.sumRange(0, 5))

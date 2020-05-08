import unittest

from l0307_range_sum_query_mutable import NumArray

class Test(unittest.TestCase):
    
    def test_solution(self):
        na = NumArray([1, 3, 5])
        self.assertEqual(9, na.sumRange(0, 2))
        na.update(1, 2)
        self.assertEqual(8, na.sumRange(0, 2))
import unittest

from l0308_range_sum_query_2d_mutable import NumMatrix

class Test(unittest.TestCase):
    
    def test_solution(self):
        nm = NumMatrix([
            [3, 0, 1, 4, 2],
            [5, 6, 3, 2, 1],
            [1, 2, 0, 1, 5],
            [4, 1, 0, 1, 7],
            [1, 0, 3, 0, 5]
        ])
        self.assertEqual(8, nm.sumRegion(2, 1, 4, 3))
        nm.update(3, 2, 2)
        self.assertEqual(10, nm.sumRegion(2, 1, 4, 3))
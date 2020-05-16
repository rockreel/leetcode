import unittest

from l0327_count_of_range_sum import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(3, Solution().countRangeSum([-2, 5, -1], -2, 2))

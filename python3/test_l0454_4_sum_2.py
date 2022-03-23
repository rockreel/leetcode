import unittest

from l0454_4_sum_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(2, Solution().fourSumCount([1,2], [-2,-1], [-1,2], [0,2]))
        self.assertEqual(1, Solution().fourSumCount([0], [0], [0], [0]))
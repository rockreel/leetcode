import unittest

from l0040_combination_sum_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]],
            Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
        self.assertEqual(
            [[1, 2, 2], [5]],
            Solution().combinationSum2([2, 5, 2, 1, 2], 5))
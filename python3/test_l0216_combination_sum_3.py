import unittest

from l0216_combination_sum_3 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual([[1, 2, 4]], sorted(Solution().combinationSum3(3, 7)))
        self.assertEqual([[1, 2, 6], [1, 3, 5], [2, 3, 4]], sorted(Solution().combinationSum3(3, 9)))

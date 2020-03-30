import unittest

from l0039_combination_sum import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual([[2, 2, 3], [7]], Solution().combinationSum([2, 3, 6, 7], 7))
        self.assertEqual([[2, 2, 2, 2], [2, 3, 3], [3, 5]], Solution().combinationSum([2, 3, 5], 8))
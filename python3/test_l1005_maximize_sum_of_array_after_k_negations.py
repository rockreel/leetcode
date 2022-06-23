import unittest

from l1005_maximize_sum_of_array_after_k_negations import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(5, Solution().largestSumAfterKNegations([4,2,3], 1))
        self.assertEqual(6, Solution().largestSumAfterKNegations([3,-1,0,2], 3))
        self.assertEqual(13, Solution().largestSumAfterKNegations([2,-3,-1,5,-4], 2))


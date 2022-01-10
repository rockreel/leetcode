import unittest

from l0494_target_sum import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            5, 
            Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))
        self.assertEqual(
            1, 
            Solution().findTargetSumWays([1], 1))

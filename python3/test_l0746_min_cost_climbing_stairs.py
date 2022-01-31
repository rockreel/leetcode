import unittest

from l0746_min_cost_climbing_stairs import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(15, Solution().minCostClimbingStairs([10, 15, 20]))
        self.assertEqual(6, Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))

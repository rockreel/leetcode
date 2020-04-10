import unittest

from l0070_climbing_stairs import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(2, Solution().climbStairs(2))
        self.assertEqual(3, Solution().climbStairs(3))
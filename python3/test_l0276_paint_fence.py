import unittest

from l0276_paint_fence import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(6, Solution().numWays(3, 2))
        self.assertEqual(4, Solution().numWays(2, 2))
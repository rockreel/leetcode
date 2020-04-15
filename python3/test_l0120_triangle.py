import unittest

from l0120_triangle import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            11,
            Solution().minimumTotal([
                [2],
                [3, 4],
                [6, 5, 7],
                [4, 1, 8, 3]
            ]))
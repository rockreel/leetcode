import unittest

from l0279_perfect_squares import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(3, Solution().numSquares(12))
        self.assertEqual(2, Solution().numSquares(13))

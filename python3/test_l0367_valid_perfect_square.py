import unittest

from l0367_valid_perfect_square import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(True, Solution().isPerfectSquare(16))
        self.assertEqual(False, Solution().isPerfectSquare(14))
        
import unittest

from l0172_factorial_trailing_zeros import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(0, Solution().trailingZeroes(3))
        self.assertEqual(1, Solution().trailingZeroes(5))
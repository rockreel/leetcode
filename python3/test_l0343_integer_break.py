import unittest

from l0343_integer_break import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(1, Solution().integerBreak(2))
        self.assertEqual(36, Solution().integerBreak(10))
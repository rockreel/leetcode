import unittest

from l0029_divide_two_integers import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(3, Solution().divide(10, 3))
        self.assertEqual(-2, Solution().divide(7, -3))
        self.assertEqual(1, Solution().divide(1, 1))
        self.assertEqual(2**31-1, Solution().divide(-2**31, -1))

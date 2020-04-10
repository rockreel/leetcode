import unittest

from l0069_sqrt_x import Solution

class Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(1, Solution().mySqrt(3))
        self.assertEqual(2, Solution().mySqrt(4))
        self.assertEqual(2, Solution().mySqrt(5))
        self.assertEqual(2, Solution().mySqrt(8))

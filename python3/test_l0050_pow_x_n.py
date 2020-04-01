import math
import unittest

from l0050_pow_x_n import Solution

class Test(unittest.TestCase):

    def test_solution(self):
        self.assertTrue(math.isclose(1024.0, Solution().myPow(2.0, 10)))
        self.assertTrue(math.isclose(9.261, Solution().myPow(2.1, 3)))
        self.assertTrue(math.isclose(0.25, Solution().myPow(2.0, -2)))
        self.assertTrue(math.isclose(0.0, Solution().myPow(2.0, -2147483648)))
import math
import unittest

from l0042_trapping_rain_water import Solution

class Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(6, Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
        self.assertEqual(2, Solution().trap([2, 0, 2]))

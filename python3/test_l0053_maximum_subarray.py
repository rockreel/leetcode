import unittest

from l0053_maximum_subarray import Solution

class Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(6, Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
        self.assertEqual(-1, Solution().maxSubArray([-1]))

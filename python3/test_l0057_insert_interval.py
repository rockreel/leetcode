import unittest

from l0057_insert_interval import Solution

class Test(unittest.TestCase):

    def test_solution(self):
        # self.assertEqual(
        #     [[1, 5], [6, 9]],
        #     Solution().insert([[1, 3], [6, 9]], [2, 5]))
        self.assertEqual(
            [[1, 2], [3, 10], [12, 16]],
            Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))


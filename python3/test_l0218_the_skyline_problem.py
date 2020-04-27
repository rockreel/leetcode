import unittest

from l0218_the_skyline_problem import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]],
            Solution().getSkyline(
                [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
            ))
        self.assertEqual(
            [[1, 3], [2, 0]],
            Solution().getSkyline(
                [[1, 2, 1], [1, 2, 2], [1, 2, 3]]
            ))
        self.assertEqual(
            [[1, 3], [5, 0]],
            Solution().getSkyline(
                [[1, 5, 3], [1, 5, 3], [1, 5, 3]]
            ))
        self.assertEqual(
            [[0, 3],[5, 0]],
            Solution().getSkyline(
                [[0, 2, 3], [2, 5, 3]]
            ))
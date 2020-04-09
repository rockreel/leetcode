import unittest

from l0054_spiral_matrix import Solution

class Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(
            [1, 2, 3, 6, 9, 8, 7, 4, 5],
            Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        self.assertEqual(
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
            Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
        self.assertEqual(
            [2, 5, 8, -1, 0, 4],
            Solution().spiralOrder([[2, 5, 8], [4, 0, -1]]))
        self.assertEqual(
            [3, 2],
            Solution().spiralOrder([[3], [2]]))

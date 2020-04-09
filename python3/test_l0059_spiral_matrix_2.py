import unittest

from l0059_spiral_matrix_2 import Solution

class Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(
            [[1, 2, 3], [8, 9, 4], [7, 6, 5]],
            Solution().generateMatrix(3))

import unittest

from l0073_set_matrix_zeros import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            [[1, 0, 1], [0, 0, 0], [1, 0, 1]],
            Solution().setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
        self.assertEqual(
            [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
            Solution().setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
        self.assertEqual(
            [[0], [0]],
            Solution().setZeroes([[1], [0]]))

            
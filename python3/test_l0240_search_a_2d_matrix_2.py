import unittest

from l0240_search_a_2d_matrix_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        matrix = [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ]
        self.assertEqual(True, Solution().searchMatrix(matrix, 5))
        self.assertEqual(False, Solution().searchMatrix(matrix, 20))

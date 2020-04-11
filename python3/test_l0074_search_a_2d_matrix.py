import unittest

from l0074_search_a_2d_matrix import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            True,
            Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 3))
        self.assertEqual(
            False,
            Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 13))
        self.assertEqual(
            False,
            Solution().searchMatrix([], 1))
        self.assertEqual(
            False,
            Solution().searchMatrix([[]], 1))
        self.assertEqual(
            True,
            Solution().searchMatrix([[1]], 1))


            
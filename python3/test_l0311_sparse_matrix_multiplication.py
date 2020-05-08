import unittest

from l0311_sparse_matrix_multiplication import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            [[7, 0, 0], [-7, 0, 3]],
            Solution().multiply([[1, 0, 0], [-1, 0, 3]], [[7, 0, 0], [0, 0, 0], [0, 0, 1]]))
        self.assertEqual(
            [[0, 1], [1, 0]],
            Solution().multiply([[1, 0], [0, 1]], [[0, 1], [1, 0]]))
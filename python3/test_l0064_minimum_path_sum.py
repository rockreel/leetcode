import unittest

from l0064_minimum_path_sum import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            7,
            Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))

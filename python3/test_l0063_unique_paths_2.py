import unittest

from l0063_unique_paths_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            2,
            Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
        self.assertEqual(
            0,
            Solution().uniquePathsWithObstacles([[0, 1]]))
        self.assertEqual(
            1,
            Solution().uniquePathsWithObstacles([[0, 1], [0, 0]]))
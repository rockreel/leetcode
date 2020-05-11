import unittest

from l0329_longest_increasing_path_in_a_matrix import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            4,
            Solution().longestIncreasingPath([
                [9, 9, 4],
                [6, 6, 8],
                [2, 1, 1],
            ]))
        self.assertEqual(
            4,
            Solution().longestIncreasingPath([
                [3, 4, 5],
                [3, 2, 6],
                [2, 2, 1],
            ]))
        self.assertEqual(
            4,
            Solution().longestIncreasingPath([
                [7, 7, 5],
                [2, 4, 6],
                [8, 2, 0],
            ]))
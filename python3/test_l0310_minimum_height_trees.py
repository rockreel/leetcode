import unittest

from l0310_minimum_height_trees import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual([1], Solution().findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]))
        self.assertEqual([3, 4], Solution().findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))

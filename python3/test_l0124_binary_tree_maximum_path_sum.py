import unittest

import common
from l0124_binary_tree_maximum_path_sum import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            6,
            Solution().maxPathSum(
                common.create_binary_tree([1, 2, 3])
            ))
        self.assertEqual(
            42,
            Solution().maxPathSum(
                common.create_binary_tree([-10, 9, 20, None, None, 15, 7])
            ))
        self.assertEqual(
            2,
            Solution().maxPathSum(
                common.create_binary_tree([2, -1])
            ))
        self.assertEqual(
            16,
            Solution().maxPathSum(
                common.create_binary_tree([9, 6, -3, None ,None, -6, 2, None, None, 2, None, -6, -6, -6])
            ))
        self.assertEqual(
            -3,
            Solution().maxPathSum(
                common.create_binary_tree([-3])
            ))
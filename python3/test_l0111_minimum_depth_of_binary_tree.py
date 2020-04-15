import unittest

import common
from l0111_minimum_depth_of_binary_tree import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            2,
            Solution().minDepth(
                common.create_binary_tree([3, 9, 20, None, None, 15, 7])
            ))
        self.assertEqual(
            2,
            Solution().minDepth(
                common.create_binary_tree([1, 2])
            ))
import unittest

import common
from l0314_binary_tree_vertical_order_traversal import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            [[9], [3, 15], [20], [7]],
            Solution().verticalOrder(
                common.create_binary_tree([3, 9, 20, None, None, 15, 7])
            ))
        self.assertEqual(
            [[4], [9], [3, 0, 1], [8], [7]],
            Solution().verticalOrder(
                common.create_binary_tree([3, 9, 8, 4, 0, 1, 7])
            ))

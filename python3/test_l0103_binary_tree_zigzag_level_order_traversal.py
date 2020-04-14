import unittest

import common
from l0103_binary_tree_zigzag_level_order_traversal import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
          [
            [3],
            [20, 9],
            [15, 7]
          ], 
          Solution().zigzagLevelOrder(common.create_binary_tree([3, 9, 20, None, None, 15, 7])))
        
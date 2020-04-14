import unittest

import common
from l0102_binary_tree_level_order_traversal import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
          [
            [3],
            [9, 20],
            [15, 7]
          ], 
          Solution().levelOrder(common.create_binary_tree([3, 9, 20, None, None, 15, 7])))
        
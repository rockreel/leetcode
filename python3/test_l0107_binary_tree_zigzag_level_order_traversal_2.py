import unittest

import common
from l0107_binary_tree_level_order_traversal_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
          [
            [15, 7],
            [9, 20],
            [3]
          ], 
          Solution().levelOrderBottom(common.create_binary_tree([3, 9, 20, None, None, 15, 7])))
        
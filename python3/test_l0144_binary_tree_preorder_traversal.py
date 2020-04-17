import unittest

import common
from l0144_binary_tree_preorder_traversal import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
          [1, 2, 3], 
          Solution().preorderTraversal(common.create_binary_tree([1, None, 2, 3])))
        
import unittest

import common
from l0094_binary_tree_inorder_traversal import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
          [1, 3, 2], 
          Solution().inorderTraversal(common.create_binary_tree([1, None, 2, 3])))
        
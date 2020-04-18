import unittest

import common
from l0145_binary_tree_postorder_traversal import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
          [3, 2, 1], 
          Solution().postorderTraversal(common.create_binary_tree([1, None, 2, 3])))

import unittest

import common
from l0285_inorder_successor_in_bst import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        root = common.create_binary_tree([1, None, 2])
        p = common.get_tree_node(root, 0)
        s = common.get_tree_node(root, 2)
        self.assertEqual(s, Solution().inorderSuccessor(root, p))

        root = common.create_binary_tree([2, 1, 3])
        p = common.get_tree_node(root, 1)
        s = common.get_tree_node(root, 0)
        self.assertEqual(s, Solution().inorderSuccessor(root, p))

import unittest

import common
from l0236_lowest_common_ancestor_of_a_binary_tree import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        tree = common.create_binary_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        p = common.get_tree_node(tree, 1)
        q = common.get_tree_node(tree, 2)
        self.assertEqual(tree, Solution().lowestCommonAncestor(tree, p, q))

        p = common.get_tree_node(tree, 1)
        q = common.get_tree_node(tree, 10)
        self.assertEqual(p, Solution().lowestCommonAncestor(tree, p, q))

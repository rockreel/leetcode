import unittest

import common
from l0235_lowest_common_ancestor_of_a_binary_search_tree import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        tree = common.create_binary_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        p = common.get_tree_node(tree, 1)
        q = common.get_tree_node(tree, 2)
        self.assertEqual(tree, Solution().lowestCommonAncestor(tree, p, q))

        p = common.get_tree_node(tree, 1)
        q = common.get_tree_node(tree, 4)
        self.assertEqual(common.get_tree_node(tree, 1), Solution().lowestCommonAncestor(tree, p, q))

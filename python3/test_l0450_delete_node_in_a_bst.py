import unittest
import common

from l0450_delete_node_in_a_bst import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            [5,4,6,2,None,None,7], 
            common.convert_binary_tree_to_list(
                Solution().deleteNode(common.create_binary_tree([5,3,6,2,4,None,7]), 3))
        )
        self.assertEqual(
            [5,3,6,2,4,None,7], 
            common.convert_binary_tree_to_list(
                Solution().deleteNode(common.create_binary_tree([5,3,6,2,4,None,7]), 0))
        )
        self.assertEqual(
            [], 
            common.convert_binary_tree_to_list(
                Solution().deleteNode(common.create_binary_tree([]), 0))
        )

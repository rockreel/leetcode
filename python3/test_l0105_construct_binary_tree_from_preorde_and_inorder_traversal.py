import unittest

import common
from l0105_construct_binary_tree_from_preorder_and_inorder_traversal import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            [3, 9, 20, None, None, 15, 7],
            common.convert_binary_tree_to_list(
                Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
            )
        )
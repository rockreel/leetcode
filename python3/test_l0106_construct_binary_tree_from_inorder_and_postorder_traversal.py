import unittest

import common
from l0106_construct_binary_tree_from_inorder_and_postorder_traversal import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            [3, 9, 20, None, None, 15, 7],
            common.convert_binary_tree_to_list(
                Solution().buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
            )
        )
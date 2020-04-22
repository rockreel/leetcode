import unittest

import common
from l0156_binary_tree_upside_down import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        # self.assertEqual(
        #     [4, 5, 2, None, None, 3, 1],
        #     common.convert_binary_tree_to_list(
        #         Solution().upsideDownBinaryTree(
        #         common.create_binary_tree([1, 2, 3, 4, 5])
        #     )))
        self.assertEqual(
            [4, None, 2, 3, 1],
            common.convert_binary_tree_to_list(
                Solution().upsideDownBinaryTree(
                common.create_binary_tree([1, 2, 3, 4])
            )))
        
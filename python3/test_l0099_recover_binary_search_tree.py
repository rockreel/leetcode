import unittest

import common
from l0099_recover_binary_search_tree import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        tree = common.create_binary_tree([1, 3, None, None, 2])
        Solution().recoverTree(tree)
        self.assertEqual(
            [3, 1, None, None, 2],
            common.convert_binary_tree_to_list(tree))

        tree = common.create_binary_tree([3, 1, 4, None, None, 2])
        Solution().recoverTree(tree)
        self.assertEqual(
            [2, 1, 4, None, None, 3],
            common.convert_binary_tree_to_list(tree))
        

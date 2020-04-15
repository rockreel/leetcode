import unittest

import common
from l0114_flatten_binary_tree_to_linked_list import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        tree = common.create_binary_tree([1, 2, 5, 3, 4, None, 6])
        Solution().flatten(tree)
        self.assertEqual(
            [1, None, 2, None, 3, None, 4, None, 5, None, 6],
            common.convert_binary_tree_to_list(tree))

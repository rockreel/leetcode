import unittest

import common
from l0095_unique_binary_search_trees_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
          sorted([
            [1, None, 3, 2],
            [3, 2, None, 1],
            [3, 1, None, None, 2],
            [2, 1, 3],
            [1, None, 2, None, 3]
          ]), 
          sorted([
            common.convert_binary_tree_to_list(t) for t in Solution().generateTrees(3)
          ]))
        self.assertEqual(
          sorted([]), 
          sorted([
            common.convert_binary_tree_to_list(t) for t in Solution().generateTrees(0)
          ]))
        
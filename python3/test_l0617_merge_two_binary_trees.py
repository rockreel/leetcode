import unittest

import common
from l0617_merge_two_binary_trees import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertTrue(
            [3,4,5,5,4,None,7],
            common.convert_binary_tree_to_list(
                Solution().mergeTrees(
                    common.create_binary_tree([1,3,2,5]), 
                    common.create_binary_tree([2,1,3,None,4,None,7])
                )
            )
        )
        self.assertTrue(
            [2, 2],
            common.convert_binary_tree_to_list(
                Solution().mergeTrees(
                    common.create_binary_tree([1]), 
                    common.create_binary_tree([1, 2])
                )
            )
        )

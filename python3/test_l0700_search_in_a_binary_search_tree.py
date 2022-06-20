import unittest
import common

from l0700_search_in_a_binary_search_tree import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            [2,1,3], 
            common.convert_binary_tree_to_list(
                Solution().searchBST(common.create_binary_tree([4,2,7,1,3]), 2))
        )
        self.assertEqual(
            [], 
            common.convert_binary_tree_to_list(
                Solution().searchBST(common.create_binary_tree([4,2,7,1,3]), 5))
        )


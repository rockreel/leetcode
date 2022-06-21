import unittest
import common

from l0669_trim_a_binary_search_tree import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            [1,None,2],
            common.convert_binary_tree_to_list(Solution().trimBST(common.create_binary_tree([1,0,2]), 1, 2)))
        self.assertEqual(
            [3,2,None,1],
            common.convert_binary_tree_to_list(Solution().trimBST(common.create_binary_tree([3,0,4,None,2,None,None,1]), 1, 3)))

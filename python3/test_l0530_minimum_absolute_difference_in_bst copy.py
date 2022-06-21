import unittest
import common

from l0538_convert_bst_to_greater_tree import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            [30,36,21,36,35,26,15,None,None,None,33,None,None,None,8], 
            common.convert_binary_tree_to_list(Solution().convertBST(
                common.create_binary_tree([4,1,6,0,2,5,7,None,None,None,3,None,None,None,8])
            )))
        self.assertEqual(
            [1,None,1], 
            common.convert_binary_tree_to_list(Solution().convertBST(
                common.create_binary_tree([0,None,1])
            )))

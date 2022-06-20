import unittest
import common

from l0701_insert_into_a_binary_search_tree import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            [4,2,7,1,3,5], 
            common.convert_binary_tree_to_list(
                Solution().insertIntoBST(common.create_binary_tree([4,2,7,1,3]), 5))
        )
        self.assertEqual(
            [40,20,60,10,30,50,70,None,None,25], 
            common.convert_binary_tree_to_list(
                Solution().insertIntoBST(common.create_binary_tree([40,20,60,10,30,50,70]), 25))
        )
        self.assertEqual(
            [4,2,7,1,3,5], 
            common.convert_binary_tree_to_list(
                Solution().insertIntoBST(common.create_binary_tree([4,2,7,1,3,None,None,None,None,None,None]), 5))
        )



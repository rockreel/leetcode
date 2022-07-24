import unittest
import common

from l0572_subtree_of_another_tree import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            True, 
            Solution().isSubtree(
                common.create_binary_tree([3, 4, 5, 1, 2]),
                common.create_binary_tree([4,1,2])))
        self.assertEqual(
            False, 
            Solution().isSubtree(
                common.create_binary_tree([3,4,5,1,2,None,None,None,None,0]),
                common.create_binary_tree([4,1,2])))

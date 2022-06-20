import unittest
import common

from l0654_maximum_binary_tree import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            [6,3,5,None,2,0,None,None,1],
            common.convert_binary_tree_to_list(Solution().constructMaximumBinaryTree([3,2,1,6,0,5])))
        self.assertEqual(
            [3,None,2,None,1],
            common.convert_binary_tree_to_list(Solution().constructMaximumBinaryTree([3,2,1])))
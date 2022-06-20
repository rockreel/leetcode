import unittest
import common

from l0530_minimum_absolute_difference_in_bst import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            1, 
            Solution().getMinimumDifference(
                common.create_binary_tree([4,2,6,1,3])
            ))
        self.assertEqual(
            1, 
            Solution().getMinimumDifference(
                common.create_binary_tree([1,0,48,None,None,12,49])
            ))


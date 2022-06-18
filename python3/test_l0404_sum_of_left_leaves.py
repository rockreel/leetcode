import unittest
from common import create_binary_tree

from l0404_sum_of_left_leaves import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            24, 
            Solution().sumOfLeftLeaves(create_binary_tree([3, 9, 20, None, None, 15, 7])))
        self.assertEqual(
            0, 
            Solution().sumOfLeftLeaves(create_binary_tree([1])))
        
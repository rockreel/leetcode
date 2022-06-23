import unittest
import common

from l0968_binary_tree_cameras import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            1, 
            Solution().minCameraCover(common.create_binary_tree([0,0,None,0,0])))
        self.assertEqual(
            2, 
            Solution().minCameraCover(common.create_binary_tree([0,0,None,0,None,0,None,None,0])))
        
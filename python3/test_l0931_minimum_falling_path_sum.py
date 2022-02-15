import unittest

from l0931_minimum_falling_path_sum import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            13, 
            Solution().minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))
        self.assertEqual(
            -59, 
            Solution().minFallingPathSum([[-19,57],[-40,-5]]))
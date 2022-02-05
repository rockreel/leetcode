import unittest

from l0994_rotting_oranges import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            4, 
            Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
        self.assertEqual(
            -1, 
            Solution().orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
        self.assertEqual(
            0, 
            Solution().orangesRotting([[0, 2]]))
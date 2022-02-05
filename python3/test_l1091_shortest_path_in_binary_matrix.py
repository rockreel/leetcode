import unittest

from l1091_shortest_path_in_binary_matrix import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            2, 
            Solution().shortestPathBinaryMatrix([[0,1],[1,0]]))
        self.assertEqual(
            4, 
            Solution().shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))
        self.assertEqual(
            -1, 
            Solution().shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]]))

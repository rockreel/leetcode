import unittest

from l0542_0_1_matrix import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            [[0, 0, 0], [0, 1, 0], [0, 0, 0]], 
            Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
        self.assertEqual(
            [[0, 0, 0], [0, 1, 0], [1, 2, 1]], 
            Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))


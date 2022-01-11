import unittest

from l0733_flood_fill import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            [[2, 2, 2], [2, 2, 0], [2, 0, 1]], 
            Solution().floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
        self.assertEqual(
            [[2, 2, 2], [2, 2, 2]], 
            Solution().floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 2))

import unittest

from l1293_shortest_path_in_a_grid_with_obstacles_elimination import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            6, 
            Solution().shortestPath([
                [0, 0, 0],
                [1, 1, 0],
                [0, 0, 0],
                [0, 1, 1],
                [0, 0, 0]
            ], 1))
        self.assertEqual(
            -1, 
            Solution().shortestPath([
                [0, 1, 1],
                [1, 1, 1],
                [1, 0, 0]
            ], 1))
        
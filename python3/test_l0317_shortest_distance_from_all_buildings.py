import unittest

from l0317_shortest_distance_from_all_buildings import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            7,
            Solution().shortestDistance([
                [1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]
            ]))
        self.assertEqual(
            1,
            Solution().shortestDistance([[1, 0], [0, 0]]))

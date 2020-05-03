import unittest

from l0286_wall_and_gates import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        rooms = [
            [2147483647, -1, 0, 2147483647],
            [2147483647, 2147483647, 2147483647, -1],
            [2147483647, -1, 2147483647, -1],
            [0, -1, 2147483647, 2147483647]
        ]
        Solution().wallsAndGates(rooms)
        self.assertEqual(
            [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]],
            rooms
        )

        rooms = [
            [0,-1],
            [2147483647,2147483647]
        ]
        Solution().wallsAndGates(rooms)
        self.assertEqual(
            [[0, -1], [1, 2]],
            rooms
        )

import unittest

from l0289_game_of_life import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        board = [
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 1],
            [0, 0, 0]
        ]
        Solution().gameOfLife(board)
        self.assertEqual(
            [
                [0, 0, 0],
                [1, 0, 1],
                [0, 1, 1],
                [0, 1, 0]
            ],
            board)
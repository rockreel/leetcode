import unittest

from l0174_dungeon_game import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        board = [
            [-2, -3, 3],
            [-5, -10, 1],
            [10, 30, -5],
        ]
        self.assertEqual(7, Solution().calculateMinimumHP(board))

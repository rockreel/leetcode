import unittest

from l0294_flip_game_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(True, Solution().canWin('++++'))
        self.assertEqual(False, Solution().canWin('+++++'))
import unittest

from l0292_nim_game import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(False, Solution().canWinNim(4))
        self.assertEqual(True, Solution().canWinNim(5))
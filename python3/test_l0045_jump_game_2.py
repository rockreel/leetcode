import unittest

from l0045_jump_game_2 import Solution

class Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(2, Solution().jump([2, 3, 1, 1, 4]))
        self.assertEqual(1, Solution().jump([3, 2, 1]))
        self.assertEqual(3, Solution().jump([3, 4, 3, 2, 5, 4, 3]))
        self.assertEqual(0, Solution().jump([0]))
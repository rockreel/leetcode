import unittest

from l0055_jump_game import Solution

class Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(True, Solution().canJump([2, 3, 1, 1, 4]))
        self.assertEqual(False, Solution().canJump([3, 2, 1, 0, 4]))

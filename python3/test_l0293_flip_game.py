import unittest

from l0293_flip_game import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            sorted([
                '--++',
                '+--+',
                '++--'
            ]),
            sorted(Solution().generatePossibleNextMoves('++++')))
        self.assertEqual(
            sorted([
                '---+++-+---+',
                '---+++---+-+',
                '---+---+++-+',
                '-----+-+++-+'
            ]),
            sorted(Solution().generatePossibleNextMoves('---+++-+++-+')))

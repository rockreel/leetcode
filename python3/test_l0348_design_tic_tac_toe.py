import unittest

from l0348_design_tic_tac_toe import TicTacToe

class Test(unittest.TestCase):
    
    def test_solution(self):
        toe = TicTacToe(3)
        self.assertEqual(0, toe.move(0, 0, 1))
        self.assertEqual(0, toe.move(0, 2, 2))
        self.assertEqual(0, toe.move(2, 2, 1))
        self.assertEqual(0, toe.move(1, 1, 2))
        self.assertEqual(0, toe.move(2, 0, 1))
        self.assertEqual(0, toe.move(1, 0, 2))
        self.assertEqual(1, toe.move(2, 1, 1))
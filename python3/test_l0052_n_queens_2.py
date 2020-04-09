import unittest

from l0052_n_queens_2 import Solution

class Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(2, Solution().totalNQueens(4))

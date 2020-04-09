import unittest

from l0051_n_queens import Solution

class Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(
            [['.Q..', '...Q', 'Q...', '..Q.'], ['..Q.', 'Q...', '...Q', '.Q..']], 
            Solution().solveNQueens(4))

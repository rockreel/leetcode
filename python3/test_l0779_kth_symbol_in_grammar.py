import unittest

from l0779_kth_symbol_in_grammar import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(0, Solution().kthGrammar(1, 1))
        self.assertEqual(0, Solution().kthGrammar(2, 1))
        self.assertEqual(1, Solution().kthGrammar(2, 2))
        
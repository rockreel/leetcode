import unittest

from l0990_satisfiability_of_equality_equations import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            False,
            Solution().equationsPossible(
                ['a==b', 'b!=a']))
        self.assertEqual(
            True,
            Solution().equationsPossible(
                ['a==b', 'b==a']))
        self.assertEqual(
            True,
            Solution().equationsPossible(
                ['a==b', 'b==c', 'a==c']))
        self.assertEqual(
            False,
            Solution().equationsPossible(
                ['a==b', 'b!=c', 'c==a']))
        self.assertEqual(
            True,
            Solution().equationsPossible(
                ['c==c', 'b==d', 'x!=z']))


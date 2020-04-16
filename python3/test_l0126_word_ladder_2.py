import unittest

from l0126_word_letter_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            sorted([
                ['hit', 'hot', 'dot', 'dog', 'cog'],
                ['hit', 'hot', 'lot', 'log', 'cog']
            ]), 
            sorted(Solution().findLadders('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog'])))
        self.assertEqual(
            sorted([]),
            sorted(Solution().findLadders('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log'])))
        self.assertEqual(
            sorted([
                ['red', 'ted', 'tad', 'tax'],
                ['red', 'ted', 'tex', 'tax'],
                ['red', 'rex', 'tex', 'tax']
            ]),
            sorted(Solution().findLadders('red', 'tax', ['ted', 'tex', 'red', 'tax', 'tad', 'den', 'rex', 'pee'])))

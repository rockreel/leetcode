import unittest

from l0127_word_letter import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(5, Solution().ladderLength('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
        self.assertEqual(0, Solution().ladderLength('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']))

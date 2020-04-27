import unittest

from l0212_word_search_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        board = [
            ['o','a','a','n'],
            ['e','t','a','e'],
            ['i','h','k','r'],
            ['i','f','l','v']
        ]
        self.assertEqual(
            ['eat', 'oath'],
            sorted(Solution().findWords(board, ['oath', 'pea', 'eat', 'rain'])))
        

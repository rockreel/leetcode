import unittest

from l0140_word_break_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            sorted(['cats and dog', 'cat sand dog']),
            sorted(Solution().wordBreak('catsanddog', ['cat', 'cats', 'and', 'sand', 'dog'])))
        self.assertEqual(
            sorted(['pine apple pen apple', 'pineapple pen apple', 'pine applepen apple']),
            sorted(Solution().wordBreak('pineapplepenapple', ['apple', 'pen', 'applepen', 'pine', 'pineapple'])))
        self.assertEqual(
            [],
            Solution().wordBreak('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']))

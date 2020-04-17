import unittest

from l0139_word_break import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(True, Solution().wordBreak('leetcode', ['leet', 'code']))
        self.assertEqual(True, Solution().wordBreak('applepenapple', ['apple', 'pen']))
        self.assertEqual(False, Solution().wordBreak('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']))

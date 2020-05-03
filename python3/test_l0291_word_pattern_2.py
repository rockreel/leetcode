import unittest

from l0291_word_pattern_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(True, Solution().wordPatternMatch('abab', 'redblueredblue'))
        self.assertEqual(True, Solution().wordPatternMatch('aaaa', 'asdasdasdasd'))
        self.assertEqual(False, Solution().wordPatternMatch('aabb', 'xyzabcxzyabc'))

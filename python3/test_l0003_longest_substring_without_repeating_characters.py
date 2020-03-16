import unittest

import common
from l0003_longest_substring_without_repeating_characters import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(3, Solution().lengthOfLongestSubstring('abcabcbb'))
        self.assertEqual(1, Solution().lengthOfLongestSubstring('bbbbb'))
        self.assertEqual(3, Solution().lengthOfLongestSubstring('pwwkew'))
import unittest

from l0340_Longest_substring_with_at_most_k_distinct_characters import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(4, Solution().lengthOfLongestSubstringKDistinct('eceba', 3))
        self.assertEqual(4, Solution().lengthOfLongestSubstringKDistinct('WORLD', 4))
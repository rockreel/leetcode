import unittest

from l0159_longest_substring_with_at_most_two_distinct_characters import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(3, Solution().lengthOfLongestSubstringTwoDistinct('aaa'))
        self.assertEqual(3, Solution().lengthOfLongestSubstringTwoDistinct('eceba'))
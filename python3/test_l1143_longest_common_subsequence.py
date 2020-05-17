import unittest

from l1143_longest_common_subsequence import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            3, 
            Solution().longestCommonSubsequence('abcde', 'ace'))
        self.assertEqual(
            3,
            Solution().longestCommonSubsequence('abc', 'abc'))
        self.assertEqual(
            0,
            Solution().longestCommonSubsequence('abc', 'def'))

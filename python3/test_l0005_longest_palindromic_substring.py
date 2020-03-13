import unittest

from l0005_longest_palindromic_substring import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual('bab', Solution().longestPalindrome('babad'))
        self.assertEqual('bb', Solution().longestPalindrome('cbbd'))
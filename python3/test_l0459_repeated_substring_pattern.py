import unittest

from l0459_repeated_substring_pattern import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(True, Solution().repeatedSubstringPattern('abab'))
        self.assertEqual(False, Solution().repeatedSubstringPattern('aba'))
        self.assertEqual(True, Solution().repeatedSubstringPattern('abcabcabcabc'))
import unittest

from l0647_palindromic_substrings import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(3, Solution().countSubstrings('abc'))
        self.assertEqual(6, Solution().countSubstrings('aaa'))

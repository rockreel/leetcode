import unittest

from l0214_shortest_palindrome import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual('aaacecaaa', Solution().shortestPalindrome('aacecaaa'))
        self.assertEqual('dcbabcd', Solution().shortestPalindrome('abcd'))

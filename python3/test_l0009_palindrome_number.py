import unittest

from l0009_palindrome_number import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(True, Solution().isPalindrome(121))
        self.assertEqual(False, Solution().isPalindrome(-121))
        self.assertEqual(False, Solution().isPalindrome(10))
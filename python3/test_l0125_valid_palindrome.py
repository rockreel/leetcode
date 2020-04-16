import unittest

from l0125_valid_palindrome import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(True, Solution().isPalindrome('A man, a plan, a canal: Panama'))
        self.assertEqual(False, Solution().isPalindrome('race a car'))
        self.assertEqual(True, Solution().isPalindrome('.,'))
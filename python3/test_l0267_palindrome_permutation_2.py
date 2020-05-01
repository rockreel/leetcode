import unittest

from l0267_palindrome_permutation_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(['abba', 'baab'], Solution().generatePalindromes('aabb'))
        self.assertEqual(['ababa', 'baaab'], Solution().generatePalindromes('aaabb'))
        self.assertEqual(['aabbaa', 'abaaba', 'baaaab'], Solution().generatePalindromes('aaaabb'))
        self.assertEqual(['civic', 'icvci'], Solution().generatePalindromes('civic'))
        self.assertEqual([], Solution().generatePalindromes('abc'))

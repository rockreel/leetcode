import unittest

from l0266_palindrome_permutation import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(False, Solution().canPermutePalindrome('code'))
        self.assertEqual(True, Solution().canPermutePalindrome('aab'))
        self.assertEqual(True, Solution().canPermutePalindrome('carerac'))
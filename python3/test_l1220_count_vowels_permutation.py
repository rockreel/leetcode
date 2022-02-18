import unittest

from l1220_count_vowels_permutation import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(5, Solution().countVowelPermutation(1))
        self.assertEqual(10, Solution().countVowelPermutation(2))
        self.assertEqual(68, Solution().countVowelPermutation(5))
        self.assertEqual(18208803, Solution().countVowelPermutation(144))

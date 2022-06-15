import unittest

from l0438_find_all_anagrams_in_a_string import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            [0, 6], 
            Solution().findAnagrams("cbaebabacd", "abc"))
        self.assertEqual(
            [0, 1, 2], 
            Solution().findAnagrams("abab", "ab"))

        
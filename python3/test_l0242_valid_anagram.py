import unittest

from l0242_valid_anagram import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(True, Solution().isAnagram('anagram', 'nagaram'))
        self.assertEqual(False, Solution().isAnagram('rat', 'car'))

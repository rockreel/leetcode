import unittest

from l0345_reverse_vowels_of_a_string import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual('holle', Solution().reverseVowels('hello'))
        self.assertEqual('leotcede', Solution().reverseVowels('leetcode'))

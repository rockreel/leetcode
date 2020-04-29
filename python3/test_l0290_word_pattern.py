import unittest

from l0290_word_pattern import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(True, Solution().wordPattern('abba', 'dog cat cat dog'))
        self.assertEqual(False, Solution().wordPattern('abba', 'dog cat cat fish'))
        self.assertEqual(False, Solution().wordPattern('aaaa', 'dog cat cat dog'))
        self.assertEqual(False, Solution().wordPattern('abba', 'dog dog dog dog'))
        self.assertEqual(False, Solution().wordPattern('abc', 'dog cat dog'))
import unittest

from l0030_substring_with_concatenation_of_all_words import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual([0, 9], Solution().findSubstring('barfoothefoobarman', ['foo', 'bar']))
        self.assertEqual([], Solution().findSubstring('wordgoodgoodgoodbestword', ['word', 'good', 'best', 'word']))
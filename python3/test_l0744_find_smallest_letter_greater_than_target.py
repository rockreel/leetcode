import unittest

from l0744_find_smallest_letter_greater_than_target import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual('c', Solution().nextGreatestLetter(['c', 'f', 'j'], 'a'))
        self.assertEqual('f', Solution().nextGreatestLetter(['c', 'f', 'j'], 'c'))
        self.assertEqual('f', Solution().nextGreatestLetter(['c', 'f', 'j'], 'd'))
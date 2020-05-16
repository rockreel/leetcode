import unittest

from l0316_remove_duplicate_letters import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual('abc', Solution().removeDuplicateLetters('bcabc'))
        self.assertEqual('acdb', Solution().removeDuplicateLetters('cbacdcbc'))

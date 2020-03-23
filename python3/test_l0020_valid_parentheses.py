import unittest

import common
from l0020_valid_parentheses import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(True, Solution().isValid('()'))
        self.assertEqual(True, Solution().isValid('()[]{}'))
        self.assertEqual(False, Solution().isValid('(]'))
        self.assertEqual(False, Solution().isValid('([)]'))
        self.assertEqual(True, Solution().isValid('{[]}'))
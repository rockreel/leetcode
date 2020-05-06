import unittest

from l0301_remove_invalid_parentheses import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(['()()()', '(())()'], Solution().removeInvalidParentheses('()())()'))
        self.assertEqual(['(a)()()', '(a())()'], Solution().removeInvalidParentheses('(a)())()'))
        self.assertEqual([''], Solution().removeInvalidParentheses(')('))

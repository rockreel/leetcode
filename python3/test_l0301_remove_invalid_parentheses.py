import unittest

from l0301_remove_invalid_parentheses import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(sorted(['()()()', '(())()']), sorted(Solution().removeInvalidParentheses('()())()')))
        self.assertEqual(sorted(['(a)()()', '(a())()']), sorted(Solution().removeInvalidParentheses('(a)())()')))
        self.assertEqual([''], Solution().removeInvalidParentheses(')('))

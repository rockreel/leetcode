import unittest

from l0032_longest_valid_parentheses import Solution

class Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(2, Solution().longestValidParentheses('(()'))
        self.assertEqual(4, Solution().longestValidParentheses(')()())'))

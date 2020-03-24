import unittest

import common
from l0022_generate_parentheses import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            ['((()))', '(()())', '(())()', '()(())', '()()()'],
            Solution().generateParenthesis(3))
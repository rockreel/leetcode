import unittest

from l0010_regular_expression_matching import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(False, Solution().isMatch('ss', 'a'))
        self.assertEqual(True, Solution().isMatch('aa', 'a*'))
import unittest

from l0150_evaluate_reverse_polish_notation import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(9, Solution().evalRPN(['2', '1', '+', '3', '*']))
        self.assertEqual(6, Solution().evalRPN(['4', '13', '5', '/', '+']))
        self.assertEqual(22, Solution().evalRPN(
            ['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+']))

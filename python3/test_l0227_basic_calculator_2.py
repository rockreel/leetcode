import unittest

from l0227_basic_calculator_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(7, Solution().calculate('3+2*2'))
        self.assertEqual(1, Solution().calculate('3/2'))
        self.assertEqual(5, Solution().calculate(' 3+5 / 2 '))
import unittest

from l0013_roman_to_integer import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(3, Solution().romanToInt('III'))
        self.assertEqual(58, Solution().romanToInt('LVIII'))
        self.assertEqual(1994, Solution().romanToInt('MCMXCIV'))

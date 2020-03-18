import unittest

from l0008_string_to_integer import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(42, Solution().myAtoi('42'))
        self.assertEqual(-42, Solution().myAtoi('  -42'))
        self.assertEqual(1, Solution().myAtoi('+1))
        self.assertEqual(4193, Solution().myAtoi('4193 with words'))
        self.assertEqual(0, Solution().myAtoi('words and 987'))
        self.assertEqual(-2147483648, Solution().myAtoi('-91283472332'))
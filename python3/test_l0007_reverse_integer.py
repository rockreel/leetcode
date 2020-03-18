import unittest

from l0007_reverse_integer import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(321, Solution().reverse(123))
        self.assertEqual(-321, Solution().reverse(-123))
        self.assertEqual(21, Solution().reverse(120))
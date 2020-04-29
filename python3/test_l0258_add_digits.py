import unittest

from l0258_add_digits import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(2, Solution().addDigits(38))

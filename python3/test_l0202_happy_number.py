import unittest

from l0202_happy_number import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(True, Solution().isHappy(19))


import unittest

from l0166_fraction_to_recurring_decimal import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual('0.5', Solution().fractionToDecimal(1, 2))
        self.assertEqual('2', Solution().fractionToDecimal(2, 1))
        self.assertEqual('0.(6)', Solution().fractionToDecimal(2, 3))
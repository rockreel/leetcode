import unittest

from l0201_bitwise_and_of_numbers_range import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(4, Solution().rangeBitwiseAnd(5, 7))
        self.assertEqual(0, Solution().rangeBitwiseAnd(0, 1))
        self.assertEqual(1, Solution().rangeBitwiseAnd(1, 1))


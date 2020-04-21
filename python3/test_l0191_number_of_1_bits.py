import unittest

from l0191_number_of_1_bits import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(3, Solution().hammingWeight(0b00000000000000000000000000001011))
        self.assertEqual(1, Solution().hammingWeight(0b00000000000000000000000010000000))
        self.assertEqual(31, Solution().hammingWeight(0b11111111111111111111111111111101))
import unittest

from l0190_reverse_bits import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(964176192, Solution().reverseBits(43261596))
        self.assertEqual(3221225471, Solution().reverseBits(4294967293))

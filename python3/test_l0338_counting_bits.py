import unittest

from l0338_counting_bits import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual([0, 1, 1], Solution().countBits(2))
        self.assertEqual([0, 1, 1, 2, 1, 2], Solution().countBits(5))
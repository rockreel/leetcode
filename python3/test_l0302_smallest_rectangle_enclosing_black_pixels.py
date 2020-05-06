import unittest

from l0302_smallest_rectangle_enclosing_black_pixels import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(6, Solution().minArea(['0010', '0110', '0100'], 0, 2))
        self.assertEqual(6, Solution().minArea(['1110', '1100', '0000', '0000'], 0, 1))


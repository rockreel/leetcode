import unittest

from l0221_maximal_square import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            4,
            Solution().maximalSquare([
                ['1', '0', '1', '0', '0'],
                ['1', '0', '1', '1', '1'],
                ['1', '1', '1', '1', '1'],
                ['1', '0', '0', '1', '0'],
            ]))

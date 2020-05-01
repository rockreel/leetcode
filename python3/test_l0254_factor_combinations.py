import unittest

from l0254_factor_combinations import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(sorted([
                [2, 6],
                [2, 2, 3],
                [3, 4]
            ]),
            Solution().getFactors(12))
        self.assertEqual(sorted([
                [2, 16],
                [2, 2, 8],
                [2, 2, 2, 4],
                [2, 2, 2, 2, 2],
                [2, 4, 4],
                [4, 8]
            ]),
            sorted(Solution().getFactors(32)))

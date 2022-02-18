import unittest

from l0790_domino_and_tromino_tiling import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(5, Solution().numTilings(3))
        self.assertEqual(1, Solution().numTilings(1))
        self.assertEqual(11, Solution().numTilings(4))
        self.assertEqual(24, Solution().numTilings(5))

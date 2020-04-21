import unittest

from l0200_number_of_islands import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            1,
            Solution().numIslands([
                ['1', '1', '1', '1', '0'],
                ['1', '1', '0', '1', '0'],
                ['1', '1', '0', '0', '0'],
                ['0', '0', '0', '0', '0'],
            ]))
        self.assertEqual(
            3,
            Solution().numIslands([
                ['1', '1', '0', '0', '0'],
                ['1', '1', '0', '0', '0'],
                ['0', '0', '1', '0', '0'],
                ['0', '0', '0', '1', '1'],
            ]))

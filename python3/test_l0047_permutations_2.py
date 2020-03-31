import unittest

from l0047_permutations_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            [[1, 1, 2], [1, 2, 1], [2, 1, 1]],
            Solution().permuteUnique([1, 1, 2]))
        self.assertEqual(
            [[0, 3, 3, 3], [3, 0, 3, 3], [3, 3, 0, 3], [3, 3, 3, 0]],
            Solution().permuteUnique([3, 3, 0, 3]))
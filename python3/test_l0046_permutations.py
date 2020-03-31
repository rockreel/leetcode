import unittest

from l0046_permutations import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
            Solution().permute([1, 2, 3]))
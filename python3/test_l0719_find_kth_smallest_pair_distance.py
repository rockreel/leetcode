import unittest

from l0719_find_kth_smallest_pair_distance import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(0, Solution().smallestDistancePair([1, 3, 1], 1))
        self.assertEqual(0, Solution().smallestDistancePair([1, 1, 1], 2))
        self.assertEqual(5, Solution().smallestDistancePair([1, 6, 1], 3))

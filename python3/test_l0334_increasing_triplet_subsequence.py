import unittest

from l0334_increasing_triplet_subsequence import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(True, Solution().increasingTriplet([1, 2, 3, 4, 5]))
        self.assertEqual(False, Solution().increasingTriplet([5, 4, 3, 2, 1]))

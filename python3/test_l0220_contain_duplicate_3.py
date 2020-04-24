import unittest

from l0220_contains_duplicate_3 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(True, Solution().containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0))
        self.assertEqual(True, Solution().containsNearbyAlmostDuplicate([1, 0, 1, 1], 1, 2))
        self.assertEqual(False, Solution().containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3))
        self.assertEqual(False, Solution().containsNearbyAlmostDuplicate([0], 0, 0))
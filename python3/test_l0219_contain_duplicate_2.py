import unittest

from l0219_contains_duplicate_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(True, Solution().containsNearbyDuplicate([1, 2, 3, 1], 3))
        self.assertEqual(True, Solution().containsNearbyDuplicate([1, 0, 1, 1], 1))
        self.assertEqual(False, Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
import unittest

from l0041_first_missing_positive import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(3, Solution().firstMissingPositive([1, 2, 0]))
        self.assertEqual(2, Solution().firstMissingPositive([3, 4, -1, 1]))
        self.assertEqual(1, Solution().firstMissingPositive([7, 8, 9, 11, 12]))
        self.assertEqual(2, Solution().firstMissingPositive([1, 1]))
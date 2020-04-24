import unittest

from l0217_contains_duplicate import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(True, Solution().containsDuplicate([1, 2, 3, 1]))
        self.assertEqual(False, Solution().containsDuplicate([1, 2, 3, 4]))
        self.assertEqual(True, Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
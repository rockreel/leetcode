import unittest

from l0081_search_in_rotated_sorted_array_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(True, Solution().search([2, 5, 6, 0, 0, 1, 2], 0))
        self.assertEqual(False, Solution().search([2, 5, 6, 0, 0, 1, 2], 3))
        self.assertEqual(True, Solution().search([1], 1))
        self.assertEqual(False, Solution().search([3, 1, 1], 0))
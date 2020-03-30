import unittest

from l0033_search_in_rotated_sorted_array import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(-1, Solution().search([0, 1, 2, 4, 5, 6, 7], 3))
        self.assertEqual(3, Solution().search([0, 1, 2, 4, 5, 6, 7], 4))
        self.assertEqual(4, Solution().search([4, 5, 6, 7, 0, 1, 2], 0))
        self.assertEqual(-1, Solution().search([4, 5, 6, 7, 0, 1, 2], 3))
        self.assertEqual(1, Solution().search([3, 1], 1))
import unittest

from l0034_find_first_and_last_position_of_element_in_sorted_array import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual([3, 4], Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
        self.assertEqual([-1, -1], Solution().searchRange([5, 7, 7, 8, 8, 10], 6))
        self.assertEqual([-1, -1], Solution().searchRange([], 0))

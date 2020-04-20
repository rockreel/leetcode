import unittest

from l0153_find_minimum_in_rotated_sorted_array import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(1, Solution().findMin([3, 4, 5, 1, 2]))
        self.assertEqual(0, Solution().findMin([4, 5, 6, 7, 0, 1, 2]))


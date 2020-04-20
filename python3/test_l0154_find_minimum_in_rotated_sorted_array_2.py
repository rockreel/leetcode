import unittest

from l0154_find_minimum_in_rotated_sorted_array_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(1, Solution().findMin([1, 3, 5]))
        self.assertEqual(0, Solution().findMin([2, 2, 2, 0, 1]))


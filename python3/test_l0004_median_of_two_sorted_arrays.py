import unittest

import common
from l0004_median_of_two_sorted_arrays import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(1.5, Solution().findMedianSortedArrays([1, 2], [-1, 3]))
        self.assertEqual(2.0, Solution().findMedianSortedArrays([1, 3], [2]))
        self.assertEqual(2.5, Solution().findMedianSortedArrays([1, 2], [3, 4]))
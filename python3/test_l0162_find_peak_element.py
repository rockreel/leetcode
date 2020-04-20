import unittest

from l0162_find_peak_element import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertTrue(Solution().findPeakElement([1, 2, 3, 1]) in [2])
        self.assertTrue(Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4]) in [1, 5])
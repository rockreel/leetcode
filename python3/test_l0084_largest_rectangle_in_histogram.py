import unittest

from l0084_largest_rectangle_in_histogram import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(10, Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))
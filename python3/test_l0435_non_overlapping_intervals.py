import unittest

from l0435_non_overlapping_intervals import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(1, Solution().eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
        self.assertEqual(2, Solution().eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
        self.assertEqual(0, Solution().eraseOverlapIntervals([[1,2],[2,3]]))
        
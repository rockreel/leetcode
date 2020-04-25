import unittest

from l0228_summary_ranges import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(['0->2', '4->5', '7'], Solution().summaryRanges([0, 1, 2, 4, 5, 7]))
        self.assertEqual(['0', '2->4', '6', '8->9'], Solution().summaryRanges([0, 2, 3, 4, 6, 8, 9]))
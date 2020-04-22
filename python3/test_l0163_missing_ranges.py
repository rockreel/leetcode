import unittest

from l0163_missing_ranges import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(['2', '4->49', '51->74', '76->99'], Solution().findMissingRanges([0, 1, 3, 50, 75], 0, 99))
        self.assertEqual(['4->6'], Solution().findMissingRanges([0, 1, 2, 3, 7], 0, 7))
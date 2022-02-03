import unittest

from l1202_smallest_string_with_swaps import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            'bacd', 
            Solution().smallestStringWithSwaps('dcab', [[0, 3], [1, 2]]))
        self.assertEqual(
            'abcd', 
            Solution().smallestStringWithSwaps('dcab', [[0, 3], [1, 2], [0, 2]]))
        self.assertEqual(
            'abc', 
            Solution().smallestStringWithSwaps('cba', [[0, 1], [1, 2]]))
        self.assertEqual(
            'ijlooqqtz', 
            Solution().smallestStringWithSwaps('otilzqqoj', [[2, 3], [7, 3], [3, 8], [1, 7], [1, 0], [0, 4], [0, 6], [3, 4], [2, 5]]))

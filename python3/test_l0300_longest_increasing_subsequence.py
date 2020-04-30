import unittest

from l0300_longest_increasing_subsequence import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(4, Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
        self.assertEqual(3, Solution().lengthOfLIS([10, 9, 2, 5, 3, 4]))
        self.assertEqual(5, Solution().lengthOfLIS([2, 15, 3, 7, 8, 6, 18]))
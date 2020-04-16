import unittest

from l0128_longest_consecutive_sequence import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(4, Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
        self.assertEqual(0, Solution().longestConsecutive([]))
        self.assertEqual(1, Solution().longestConsecutive([0]))

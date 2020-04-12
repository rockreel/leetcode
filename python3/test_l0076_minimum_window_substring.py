import unittest

from l0076_minimum_window_substring import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual('BANC', Solution().minWindow('ADOBECODEBANC', 'ABC'))
        self.assertEqual('', Solution().minWindow('A', 'AA'))
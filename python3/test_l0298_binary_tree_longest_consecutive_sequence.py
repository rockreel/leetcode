import unittest

import common
from l0298_binary_tree_longest_consecutive_sequence import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            3,
            Solution().longestConsecutive(
                common.create_binary_tree([1, None, 3, 2, 4, None, None, None, 5])
            ))
        self.assertEqual(
            2,
            Solution().longestConsecutive(
                common.create_binary_tree([2, None, 3, 2, None, 1])
            ))
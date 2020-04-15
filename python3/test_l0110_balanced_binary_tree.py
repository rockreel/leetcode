import unittest

import common
from l0110_balanced_binary_tree import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            True,
            Solution().isBalanced(
                common.create_binary_tree([3, 9, 20, None, None, 15, 7])
            ))
        self.assertEqual(
            False,
            Solution().isBalanced(
                common.create_binary_tree([1, 2, 2, 3, 3, None, None, 4, 4])
            ))
        self.assertEqual(
            False,
            Solution().isBalanced(
                common.create_binary_tree([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, None, None, 5, 5])
            ))
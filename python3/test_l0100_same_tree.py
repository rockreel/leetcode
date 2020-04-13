import unittest

import common
from l0100_same_tree import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            True,
            Solution().isSameTree(
                common.create_binary_tree([1, 2, 3]),
                common.create_binary_tree([1, 2, 3])
            ))
        self.assertEqual(
            False,
            Solution().isSameTree(
                common.create_binary_tree([1, 2]),
                common.create_binary_tree([1, None, 2])
            ))
        self.assertEqual(
            False,
            Solution().isSameTree(
                common.create_binary_tree([1, 2, 1]),
                common.create_binary_tree([1, 1, 2])
            ))
        
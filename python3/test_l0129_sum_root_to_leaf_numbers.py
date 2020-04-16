import unittest

import common
from l0129_sum_root_to_leaf_numbers import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            25,
            Solution().sumNumbers(
                common.create_binary_tree([1, 2, 3])
            ))
        self.assertEqual(
            1026,
            Solution().sumNumbers(
                common.create_binary_tree([4, 9, 0, 5, 1])
            ))
        self.assertEqual(
            0,
            Solution().sumNumbers(
                common.create_binary_tree([])
            ))
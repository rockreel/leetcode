import unittest

import common
from l0230_kth_smallest_element_in_a_bst import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            1,
            Solution().kthSmallest(
                common.create_binary_tree([3, 1, 4, None, 2]), 1
            ))
        self.assertEqual(
            3,
            Solution().kthSmallest(
                common.create_binary_tree([5, 3, 6, 2, 4, None, None, 1]), 3
            ))

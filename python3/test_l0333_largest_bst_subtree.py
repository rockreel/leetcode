import unittest

import common
from l0333_largest_bst_subtree import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            4,
            Solution().largestBSTSubtree(
                common.create_binary_tree([10, 5, 15, 1, 8, None, 7])
            ))

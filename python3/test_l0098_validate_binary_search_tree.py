import unittest

import common
from l0098_validate_binary_search_tree import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            True,
            Solution().isValidBST(
                common.create_binary_tree([2, 1, 3])
            ))
        self.assertEqual(
            False,
            Solution().isValidBST(
                common.create_binary_tree([5, 1, 4, None, None, 3, 6])
            ))
        self.assertEqual(
            False,
            Solution().isValidBST(
                common.create_binary_tree([1, 1])
            ))

import unittest

import common
from l0250_count_univalue_subtrees import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            4,
            Solution().countUnivalSubtrees(
                common.create_binary_tree([5, 1, 5, 5, 5, None, 5])
            ))
        self.assertEqual(
            3,
            Solution().countUnivalSubtrees(
                common.create_binary_tree([1, 3, 2, 4, 5, None, 6])
            ))

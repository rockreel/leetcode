import unittest

import common
from l0112_path_sum import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            True,
            Solution().hasPathSum(
                common.create_binary_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]),
                22
            ))
        self.assertEqual(
            False,
            Solution().hasPathSum(
                common.create_binary_tree([]),
                0
            ))

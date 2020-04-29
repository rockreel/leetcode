import unittest

import common
from l0257_binary_tree_paths import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            ['1->2->5', '1->3'],
            Solution().binaryTreePaths(
                common.create_binary_tree([1, 2, 3, None, 5])
            ))

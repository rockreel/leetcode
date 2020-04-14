import unittest

import common
from l0104_maximum_depth_of_binary_tree import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            3,
            Solution().maxDepth(
                common.create_binary_tree([3, 9, 20, None, None, 15, 7])
            ))
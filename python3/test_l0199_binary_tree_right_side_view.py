import unittest

import common
from l0199_binary_tree_right_side_view import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            [1, 3, 4],
            Solution().rightSideView(
                common.create_binary_tree([1, 2, 3, None, 5, None, 4])
            ))
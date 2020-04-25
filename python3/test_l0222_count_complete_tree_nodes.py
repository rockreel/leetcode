import unittest

import common
from l0222_count_complete_tree_nodes import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            6,
            Solution().countNodes(
                common.create_binary_tree([1, 2, 3, 4, 5, 6])
            ))
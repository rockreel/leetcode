import unittest

import common
from l0226_invert_binary_tree import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            [4, 7, 2, 9, 6, 3, 1],
            common.convert_binary_tree_to_list(
                Solution().invertTree(
                common.create_binary_tree([4, 2, 7, 1, 3, 6, 9])
            )))

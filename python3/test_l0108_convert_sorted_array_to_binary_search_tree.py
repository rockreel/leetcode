import unittest

import common
from l0108_convert_sorted_array_to_binary_search_tree import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            [0, -3, 9, -10, None, 5],
            common.convert_binary_tree_to_list(
                Solution().sortedArrayToBST([-10, -3 ,0, 5, 9])
            )
        )
import unittest

import common
from l0272_closest_binary_search_tree_value_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            [1],
            Solution().closestKValues(
                common.create_binary_tree([1]), 0.0, 1
            ))
        self.assertEqual(
            sorted([1, 2]),
            sorted(Solution().closestKValues(
                common.create_binary_tree([3, 1, 4, 0, 2]), 1.5, 2
            )))
        self.assertEqual(
            sorted([1, 2, 3]),
            sorted(Solution().closestKValues(
                common.create_binary_tree([3, 2, 5, 1]), 1.0, 3
            )))

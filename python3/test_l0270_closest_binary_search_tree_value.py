import unittest

import common
from l0270_closest_binary_search_tree_value import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            5,
            Solution().closestValue(
                common.create_binary_tree([5, 4, 9, 2, None, 8, 10]), 6.124780
            ))
        self.assertEqual(
            4,
            Solution().closestValue(
                common.create_binary_tree([3, 2, 4, 1]), 4.142857
            ))

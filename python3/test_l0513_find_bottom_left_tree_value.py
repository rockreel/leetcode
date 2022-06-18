import unittest

from common import create_binary_tree

from l0513_find_bottom_left_tree_value import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(1, Solution().findBottomLeftValue(create_binary_tree([2, 1, 3])))
        self.assertEqual(7, Solution().findBottomLeftValue(create_binary_tree([1, 2, 3, 4, None, 5, 6, None, None, 7])))

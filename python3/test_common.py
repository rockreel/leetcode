import unittest

from common import *

class Test(unittest.TestCase):
    
    def test_binary_tree(self):
        self.assertEqual(
            [],
            convert_binary_tree_to_list(
                create_binary_tree([])))
        self.assertEqual(
            [1, 2, 3],
            convert_binary_tree_to_list(
                create_binary_tree([1, 2, 3])))
        self.assertEqual(
            [1, None, 2, 3],
            convert_binary_tree_to_list(
                create_binary_tree([1, None, 2, 3])))
        self.assertEqual(
            [5, 4, 7, 3, None, 2, None, -1, None, 9],
            convert_binary_tree_to_list(
                create_binary_tree([5, 4, 7, 3, None, 2, None, -1, None, 9])))

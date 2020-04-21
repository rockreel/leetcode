import unittest

import common
from l0173_binary_search_tree_iterator import BSTIterator

class Test(unittest.TestCase):
    
    def test_solution(self):
        root = common.create_binary_tree([7, 3, 15, None, None, 9, 20])
        iterator = BSTIterator(root)
        self.assertEqual(3, iterator.next())
        self.assertEqual(7, iterator.next())
        self.assertTrue(iterator.hasNext())
        self.assertEqual(9, iterator.next())
        self.assertTrue(iterator.hasNext())
        self.assertEqual(15, iterator.next())
        self.assertTrue(iterator.hasNext())
        self.assertEqual(20, iterator.next())
        self.assertFalse(iterator.hasNext())
        
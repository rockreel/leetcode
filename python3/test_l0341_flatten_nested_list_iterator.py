import unittest

from l0341_flatten_nested_list_iterator import NestedInteger
from l0341_flatten_nested_list_iterator import NestedIterator

class Test(unittest.TestCase):
    
    def test_solution(self):
        nit = NestedIterator([
            NestedInteger([NestedInteger(1), NestedInteger(1)]),
            NestedInteger(2),
            NestedInteger([NestedInteger(1), NestedInteger(1)])])
        self.assertEqual(1, nit.next())
        self.assertEqual(1, nit.next())
        self.assertEqual(2, nit.next())
        self.assertEqual(1, nit.next())
        self.assertEqual(1, nit.next())
        self.assertEqual(False, nit.hasNext())
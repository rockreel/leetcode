import unittest

from l0339_nested_list_weight_sum import Solution
from l0339_nested_list_weight_sum import NestedInteger

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            10,
            Solution().depthSum([
                NestedInteger([NestedInteger(1), NestedInteger(1)]),
                NestedInteger(2),
                NestedInteger([NestedInteger(1), NestedInteger(1)])
            ]))
        self.assertEqual(
            27,
            Solution().depthSum([
                NestedInteger(1),
                NestedInteger([NestedInteger(4), NestedInteger([NestedInteger(6)])])]))
import unittest

import common
from l0160_intersection_of_two_linked_lists import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        l1 = common.create_linked_list([1, 2])
        l2 = common.create_linked_list([4, 5, 6])
        l3 = common.create_linked_list([7, 8])
        common.get_node(l1, 1).next = l3
        common.get_node(l2, 2).next = l3
        self.assertEqual(l3, Solution().getIntersectionNode(l1, l2))

        l1 = common.create_linked_list([1, 2, 3])
        l2 = common.create_linked_list([4])
        l3 = common.create_linked_list([5, 6])
        common.get_node(l1, 2).next = l3
        common.get_node(l2, 0).next = l3
        self.assertEqual(l3, Solution().getIntersectionNode(l1, l2))

        l1 = common.create_linked_list([1, 2, 3])
        l2 = common.create_linked_list([4, 5])
        self.assertEqual(None, Solution().getIntersectionNode(l1, l2))

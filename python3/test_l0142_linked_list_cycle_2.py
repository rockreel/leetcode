import unittest

import common
from l0142_linked_list_cycle_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        l = common.create_linked_list([1, 2, 3, 4])
        end_node = common.get_linked_list_node(l, 3)
        end_node.next = common.get_linked_list_node(l, 1)
        self.assertEqual(common.get_linked_list_node(l, 1), Solution().detectCycle(l))

        l = common.create_linked_list([1, 2])
        end_node = common.get_linked_list_node(l, 1)
        end_node.next = common.get_linked_list_node(l, 0)
        self.assertEqual(common.get_linked_list_node(l, 0), Solution().detectCycle(l))

        self.assertEqual(None, Solution().detectCycle(common.create_linked_list([1])))
        

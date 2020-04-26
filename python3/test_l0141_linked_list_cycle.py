import unittest

import common
from l0141_linked_list_cycle import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        l = common.create_linked_list([1, 2, 3, 4])
        end_node = common.get_linked_list_node(l, 3)
        end_node.next = common.get_linked_list_node(l, 1)
        self.assertEqual(True, Solution().hasCycle(l))

        l = common.create_linked_list([1, 2])
        end_node = common.get_linked_list_node(l, 1)
        end_node.next = common.get_linked_list_node(l, 0)
        self.assertEqual(True, Solution().hasCycle(l))

        self.assertEqual(False, Solution().hasCycle(common.create_linked_list([1])))
        

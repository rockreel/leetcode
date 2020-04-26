import unittest

import common
from l0237_delete_node_in_a_linked_list import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        l = common.create_linked_list([4, 5, 1, 9])
        Solution().deleteNode(common.get_linked_list_node(l, 1))
        self.assertEqual(
            [4, 1, 9],
            common.convert_linked_list_to_list(l)
        )

        l = common.create_linked_list([4, 5, 1, 9])
        Solution().deleteNode(common.get_linked_list_node(l, 2))
        self.assertEqual(
            [4, 5, 9],
            common.convert_linked_list_to_list(l)
        )

import unittest

import common
from l0143_reorder_list import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        l = common.create_linked_list([1, 2, 3, 4])
        Solution().reorderList(l)
        self.assertEqual([1, 4, 2, 3], common.convert_linked_list_to_list(l))

        l = common.create_linked_list([1, 2, 3, 4, 5])
        Solution().reorderList(l)
        self.assertEqual([1, 5, 2, 4, 3], common.convert_linked_list_to_list(l))

        l = common.create_linked_list([])
        Solution().reorderList(l)
        self.assertEqual([], common.convert_linked_list_to_list(l))

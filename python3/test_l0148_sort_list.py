import unittest

import common
from l0148_sort_list import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            [1, 2, 3, 4],
            common.convert_linked_list_to_list(
                Solution().sortList(common.create_linked_list([4, 2, 1, 3])))
        )
        self.assertEqual(
            [-1, 0, 3, 4, 5],
            common.convert_linked_list_to_list(
                Solution().sortList(common.create_linked_list([-1, 5, 3, 4, 0])))
        )
        self.assertEqual(
            [],
            common.convert_linked_list_to_list(
                Solution().sortList(common.create_linked_list([])))
        )

import unittest

import common
from l0023_merge_k_sorted_list import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        lists = [
            common.create_linked_list([1, 4, 5]),
            common.create_linked_list([1, 3, 4]),
            common.create_linked_list([2, 6]),
        ]
        self.assertEqual(
          [1, 1, 2, 3, 4, 4, 5, 6], 
          common.convert_linked_list_to_list(Solution().mergeKLists(lists)))
        lists = [
            common.create_linked_list([]),
            common.create_linked_list([1]),
        ]
        self.assertEqual(
          [1], 
          common.convert_linked_list_to_list(Solution().mergeKLists(lists)))
import unittest

import common
from l0021_merge_two_sorted_list import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
          [1, 1, 2, 3, 4, 4], 
          common.convert_linked_list_to_list(
            Solution().mergeTwoLists(
              common.create_linked_list([1, 2, 4]),
              common.create_linked_list([1, 3, 4]))))
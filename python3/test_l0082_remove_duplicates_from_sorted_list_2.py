import unittest

import common
from l0082_remove_duplicates_from_sorted_list_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
          [1, 2, 5], 
          common.convert_linked_list_to_list(
            Solution().deleteDuplicates(common.create_linked_list([1, 2, 3, 3, 4, 4, 5]))))
        self.assertEqual(
          [2, 3], 
          common.convert_linked_list_to_list(
            Solution().deleteDuplicates(common.create_linked_list([1, 1, 1, 2, 3]))))
        self.assertEqual(
          [], 
          common.convert_linked_list_to_list(
            Solution().deleteDuplicates(common.create_linked_list([1, 1]))))


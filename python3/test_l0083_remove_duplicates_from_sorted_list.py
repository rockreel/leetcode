import unittest

import common
from l0083_remove_duplicates_from_sorted_list import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
          [1, 2], 
          common.convert_linked_list_to_list(
            Solution().deleteDuplicates(common.create_linked_list([1, 1, 2]))))
        self.assertEqual(
          [1, 2, 3], 
          common.convert_linked_list_to_list(
            Solution().deleteDuplicates(common.create_linked_list([1, 1, 2, 3, 3]))))


import unittest

import common
from l0025_reverse_nodes_in_k_group import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
          [2, 1, 4, 3, 5], 
          common.convert_linked_list_to_list(
            Solution().reverseKGroup(common.create_linked_list([1, 2, 3, 4, 5]), 2)))
        self.assertEqual(
          [3, 2, 1, 4, 5], 
          common.convert_linked_list_to_list(
            Solution().reverseKGroup(common.create_linked_list([1, 2, 3, 4, 5]), 3)))
        self.assertEqual(
          [2, 1], 
          common.convert_linked_list_to_list(
            Solution().reverseKGroup(common.create_linked_list([1, 2]), 2)))

import unittest

import common
from l0061_rotate_list import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
          [4, 5, 1, 2, 3], 
          common.convert_linked_list_to_list(
            Solution().rotateRight(common.create_linked_list([1, 2, 3, 4, 5]), 2)))
        self.assertEqual(
          [2, 0, 1], 
          common.convert_linked_list_to_list(
            Solution().rotateRight(common.create_linked_list([0, 1, 2]), 4)))
        self.assertEqual(
          [1], 
          common.convert_linked_list_to_list(
            Solution().rotateRight(common.create_linked_list([1]), 1)))

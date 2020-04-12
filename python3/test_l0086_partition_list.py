import unittest

import common
from l0086_partition_list import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
          [1, 2, 2, 4, 3, 5], 
          common.convert_linked_list_to_list(
            Solution().partition(common.create_linked_list([1, 4, 3, 2, 5, 2]), 3)))
        
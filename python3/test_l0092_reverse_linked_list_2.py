import unittest

import common
from l0092_reverse_linked_list_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
          [1, 4, 3, 2, 5], 
          common.convert_linked_list_to_list(
            Solution().reverseBetween(common.create_linked_list([1, 2, 3, 4, 5]), 2, 4)))
        
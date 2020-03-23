import unittest

import common
from l0019_remove_nth_node_from_end_of_list import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
          [1, 2, 3, 5], 
          common.convert_linked_list_to_list(
            Solution().removeNthFromEnd(common.create_linked_list([1, 2, 3, 4, 5]),2)))


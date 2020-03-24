import unittest

import common
from l0024_swap_nodes_in_pairs import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
          [2, 1, 4, 3], 
          common.convert_linked_list_to_list(
            Solution().swapPairs(common.create_linked_list([1, 2, 3, 4]))))

import unittest

import common
from l0328_odd_even_linked_list import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            [1, 3, 5, 2, 4],
            common.convert_linked_list_to_list(
                Solution().oddEvenList(common.create_linked_list([1, 2, 3, 4, 5]))))
        self.assertEqual(
            [2, 3, 6, 7, 1, 5, 4],
            common.convert_linked_list_to_list(
                Solution().oddEvenList(common.create_linked_list([2, 1, 3, 5, 6, 4, 7]))))

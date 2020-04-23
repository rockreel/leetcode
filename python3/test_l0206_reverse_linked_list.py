import unittest

import common
from l0206_reverse_linked_list import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            [5, 4, 3, 2, 1],
            common.convert_linked_list_to_list(
                Solution().reverseList(common.create_linked_list([1, 2, 3, 4, 5])))
        )

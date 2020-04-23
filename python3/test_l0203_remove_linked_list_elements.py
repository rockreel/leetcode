import unittest

import common
from l0203_remove_linked_list_elements import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            [1, 2, 3, 4, 5], 
            common.convert_linked_list_to_list(
                Solution().removeElements(common.create_linked_list([1, 2, 6, 3, 4, 5, 6]), 6)))



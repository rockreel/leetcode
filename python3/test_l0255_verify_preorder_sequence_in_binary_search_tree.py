import unittest

import common
from l0255_verify_preorder_sequence_in_binary_search_tree import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(True, Solution().verifyPreorder([1, 3, 2]))
        self.assertEqual(False, Solution().verifyPreorder([3, 2, 4, 1]))
import unittest

import common
from l0331_verify_preorder_serialization_of_a_binary_tree import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            True,
            Solution().isValidSerialization('9,3,4,#,#,1,#,#,2,#,6,#,#'))
        self.assertEqual(
            False,
            Solution().isValidSerialization('1,#'))
        self.assertEqual(
            False,
            Solution().isValidSerialization('9,#,#,1'))

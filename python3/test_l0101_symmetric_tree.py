import unittest

import common
from l0101_symmetic_tree import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            True,
            Solution().isSymmetric(
                common.create_binary_tree([1, 2, 2, 3, 4, 4, 3])
            ))
        self.assertEqual(
            False,
            Solution().isSymmetric(
                common.create_binary_tree([1, 2, 2, None, 3, None, 3])
            ))
        
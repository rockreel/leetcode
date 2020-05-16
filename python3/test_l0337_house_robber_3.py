import unittest

import common
from l0337_house_robber_3 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            7,
            Solution().rob(common.create_binary_tree([3, 2, 3, None, 3, None, 1])))
        self.assertEqual(
            9,
            Solution().rob(common.create_binary_tree([3, 4, 5, 1, 3, None, 1])))


import unittest

import common
from l0113_path_sum_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            [
                [5, 4, 11, 2],
                [5, 8, 4, 5]
            ],
            Solution().pathSum(
                common.create_binary_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]),
                22
            ))

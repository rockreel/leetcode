import unittest

from l0325_maximum_size_subarray_sum_equals_k import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(4, Solution().maxSubArrayLen([1, -1, 5, -2, 3], 3))
        self.assertEqual(2, Solution().maxSubArrayLen([-2, -1, 2, 1], 1))
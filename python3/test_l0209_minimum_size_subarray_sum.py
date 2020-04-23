import unittest

from l0209_minimum_size_subarray_sum import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(2, Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))


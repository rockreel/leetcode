import unittest

from l0918_maximum_sum_circular_subarray import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            3, 
            Solution().maxSubarraySumCircular([1,-2,3,-2]))
        self.assertEqual(
            10, 
            Solution().maxSubarraySumCircular([5,-3,5]))
        self.assertEqual(
            -2, 
            Solution().maxSubarraySumCircular([-3,-2,-3]))
        
        
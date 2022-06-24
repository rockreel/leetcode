import unittest

from l0416_partition_equal_subset_sum import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            True, 
            Solution().canPartition([1,5,11,5]))
        self.assertEqual(
            False, 
            Solution().canPartition([1,2,3,5]))
        
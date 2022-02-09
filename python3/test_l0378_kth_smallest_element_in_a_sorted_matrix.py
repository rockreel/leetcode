import unittest

from l0378_kth_smallest_element_in_a_sorted_matrix import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(13, Solution().kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))
        self.assertEqual(-5, Solution().kthSmallest([[-5]], 1))

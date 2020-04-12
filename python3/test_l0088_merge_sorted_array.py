import unittest

from l0088_merge_sorted_array import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        nums2 = [2, 5, 6]
        Solution().merge(nums1, 3, nums2, 3)
        self.assertEqual([1, 2, 2, 3, 5, 6], nums1)


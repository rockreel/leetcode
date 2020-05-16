from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        for n in nums1_set:
            if n in nums2_set:
                result.append(n)
        return result

from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def max_num(nums: List[int], k: int) -> List[int]:
            result = []
            # How many number can be removed.
            counter = len(nums) - k
            for n in nums:
                while counter > 0 and result and result[-1] < n:
                    result.pop()
                    counter -= 1
                result.append(n)
            return result[:k]
            
        def merge(nums1: List[int], nums2: List[int]) -> List[int]:
            i1, i2, k = 0, 0, 0
            result = []
            while k < len(nums1) + len(nums2):
                if nums1[i1:] > nums2[i2:]:
                    result.append(nums1[i1])
                    i1 += 1
                else:
                    result.append(nums2[i2])
                    i2 += 1
                k += 1
            return result
        
        # Take i numbers from nums1.
        result = []
        for i in range(max(0, k-len(nums2)), min(k, len(nums1))+1):
            result = max(
                result,
                merge(max_num(nums1, i), max_num(nums2, k-i)))
        
        return result
        

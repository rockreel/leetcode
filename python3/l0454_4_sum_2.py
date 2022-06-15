from collections import defaultdict
from typing import List

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        index_map_1 = defaultdict(int)
        for i1, n1 in enumerate(nums1):
            for i2, n2 in enumerate(nums2):
                index_map_1[n1+n2] += 1
        index_map_2 = defaultdict(int)
        for i3, n3 in enumerate(nums3):
            for i4, n4 in enumerate(nums4):
                index_map_2[n3+n4] += 1
        count = 0        
        for k1, v1 in index_map_1.items():
            if -k1 in index_map_2:
                count += v1 * index_map_2[-k1]
        return count
    
    def fourSumCount2(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        result = 0
        sum_count = defaultdict(int)
        for n1 in nums1:
            for n2 in nums2:
                sum_count[n1 + n2] += 1
        for n3 in nums3:
            for n4 in nums4:
                result += sum_count[-n3-n4]
        return result
import bisect
from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        nums_sorted = []
        result = []
        for i in range(len(nums)-1, -1, -1):
            pos = bisect.bisect_left(nums_sorted, nums[i])
            result.append(pos)
            nums_sorted.insert(pos, nums[i])
        return result[::-1]

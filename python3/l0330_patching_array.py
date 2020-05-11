from typing import List

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # sum_to is the lowest number array can NOT sum to.
        sum_to, added = 1, 0
        i = 0
        while sum_to <= n:
            if i < len(nums) and nums[i] <= sum_to:
                sum_to += nums[i]
                i += 1
            else:
                sum_to += sum_to
                added += 1
        return added

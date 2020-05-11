from typing import List

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # sum_to is the lowest number array can NOT sum to.
        sum_to, added = 1, 0
        i = 0
        while sum_to <= n:
            if i < len(nums) and nums[i] <= sum_to:
                # If there is num less or equal to sum_to, then
                # sum_to can be extended to sum_to + num[i].
                sum_to += nums[i]
                i += 1
            else:
                # If need to add a number, then add sum_to to array
                # so range can be extended most.
                sum_to += sum_to
                added += 1
        return added

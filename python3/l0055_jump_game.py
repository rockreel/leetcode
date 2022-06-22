from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        i = 0
        while i <= max_reach:
            max_reach = max(max_reach, nums[i] + i)
            i += 1
            if max_reach >= len(nums) - 1:
                return True

        return False
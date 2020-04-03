from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0
        for i, n in enumerate(nums):
            max_jump = max(max_jump - 1, n)
            if max_jump == 0:
                break
        
        return i == len(nums) - 1
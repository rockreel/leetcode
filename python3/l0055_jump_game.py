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

    def canJumpDP(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[0] = True
        
        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1):
                if nums[j] + j >= i and dp[j]:
                    dp[i] = True
                    break

        return dp[-1]
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i]: max money can rob from nums[:i].
        dp = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            dp[i] = max(dp[i-1], nums[i-1] + dp[i-2])
            
        return dp[-1]


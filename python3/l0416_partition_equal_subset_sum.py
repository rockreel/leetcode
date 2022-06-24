from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2

        # dp[i][j]: a subset exists from nums[:i+1] that sum up to j.
        dp = [[False] * (target + 1) for _ in nums]
        if nums[0] <= target:
            dp[0][nums[0]] = True
        else:
            return False
            
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] = dp[i-1][j] or (j-nums[i] >= 0 and dp[i-1][j-nums[i]])
        return dp[-1][-1]
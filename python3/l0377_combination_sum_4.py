from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # dp[i]: target i
        dp = [0] * (target + 1)
        dp[0] = 1
        for j in range(1, len(dp)):
            for i in range(len(nums)):
                if j - nums[i] >= 0:
                    dp[j] += dp[j-nums[i]]

        return dp[-1]
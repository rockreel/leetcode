from typing import List

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        m = max(nums)
        dp = [0] * max(m, 2)
        num_count = [0] * max(m, 2)
        for n in nums:
            num_count[n-1] += 1
        dp[0] = num_count[0]
        dp[1] = max(dp[0], num_count[1] * 2)
        for i in range(2, m):
            dp[i] = max(dp[i-1], dp[i-2] + num_count[i] * (i+1))
        return dp[m-1]
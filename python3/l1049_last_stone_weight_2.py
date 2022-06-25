from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = sum(stones) // 2
        dp = [[0] * (target + 1) for _ in stones]
        for j in range(stones[0], len(dp[0])):     
            dp[0][j] = stones[0]
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if j >= stones[i]:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-stones[i]] + stones[i])
                else:
                    dp[i][j] = dp[i-1][j]
        return sum(stones) - 2 * dp[-1][-1]

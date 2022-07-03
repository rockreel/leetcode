from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i][j]: with coins[:i+1] coins and j amount.
        dp = [[0] * (amount + 1) for _ in coins]
        for i in range(len(dp)):
            dp[i][0] = 1
        for j in range(len(dp[0])):
            if j % coins[0] == 0:
                dp[0][j] = 1
        for i in range(1, len(dp)):
            for j in range(len(dp[0])):
                dp[i][j] = dp[i-1][j]
                if j-coins[i] >= 0:
                    dp[i][j] += dp[i][j-coins[i]]
        return dp[-1][-1]
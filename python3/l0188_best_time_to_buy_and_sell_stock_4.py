from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # dp[i][j]: max profit at ith day with j transaction remaining, hold or not hold a stock.
        dp_hold = [[0] * (k+1) for _ in range(len(prices)+1)]
        dp_not_hold = [[0] * (k+1) for _ in range(len(prices)+1)]
        for i in range(len(prices)-1, -1, -1):
            for j in range(1, k+1):
                dp_hold[i][j] = max(dp_hold[i+1][j], prices[i] + dp_not_hold[i+1][j-1])
                dp_not_hold[i][j] = max(dp_not_hold[i+1][j], -prices[i] + dp_hold[i+1][j])
        return dp_not_hold[0][k]
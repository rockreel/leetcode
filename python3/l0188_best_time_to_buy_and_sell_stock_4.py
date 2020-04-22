from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k >= len(prices) // 2:
            # Trades more than prices, just sum every price up.
            max_profit = 0
            for i in range(len(prices)-1):
                max_profit += max(prices[i+1] - prices[i], 0)
            return max_profit

        # For trades less than prices use dynamic programing.
        # dp[i][j]: max profit with i trades on prices[:j]
        dp = [[0 for _ in range(len(prices)+1)] for _ in range(k+1)]

        for i in range(1, min(k + 1, len(prices) // 2 + 2)):
            max_protential_profit = float('-inf')
            for j in range(2, len(prices)+1):
                max_protential_profit = max(
                    dp[i-1][j-2] - prices[j-2],  # After profit before prices[j-2], buy at prices[j-2]
                    max_protential_profit
                )
                dp[i][j] = max(
                    max_protential_profit + prices[j-1],  # Sell at prices[j-1]
                    dp[i][j-1]  # No trade on prices[j-1]
                )
                # For reference only.
                # for l in range(j-1):
                #     max_profit =  max(max_profit, dp[i-1][l] - prices[l])
                
        return dp[-1][-1]
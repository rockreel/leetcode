from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [-1] * (amount + 1)
        coins = sorted(coins)
        if coins[0] < 0 or coins[0] > amount:
            return -1
        dp[0] = 0
        for i in range(1, len(dp)):
            min_coin = float('inf')
            for c in coins:
                if i - c >= 0 and dp[i-c] != -1:
                    min_coin = min(min_coin, dp[i-c] + 1)
            dp[i] = min_coin if min_coin != float('inf') else -1
        return dp[-1]
        

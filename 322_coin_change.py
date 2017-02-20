class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # minimum coins for i amount.
        dp = [0] * (amount + 1)
        for i in range(1, len(dp)):
            num_coins = [dp[i-c]+1 for c in coins if i - c >= 0 and dp[i-c] != -1]
            dp[i] = min(num_coins) if num_coins else -1
        return dp[-1]


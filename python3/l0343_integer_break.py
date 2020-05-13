class Solution:
    def integerBreak(self, n: int) -> int:
        # dp[i]: max product of i + 1
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            max_product = 0
            for k in range(i):
                max_product = max([max_product, dp[k]*(i-k), (k+1)*(i-k)])
            dp[i] = max_product
        return dp[-1]        

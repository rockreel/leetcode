class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j]: number of subseq of s[:i] and t[:j]
        dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
        for i in range(len(s)+1):
            dp[i][0] = 1
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]

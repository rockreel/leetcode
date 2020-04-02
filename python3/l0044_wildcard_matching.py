class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def isCharMatch(s, p):
            return p == '?' or p == '*' or s == p

        # dp[i][j]: p[:i] matches s[:j].
        dp = [[False for _ in range(len(s)+1)] for _ in range(len(p)+1)]
        dp[0][0] = True
        for i in range(1, len(p)+1):
            dp[i][0] = p[i-1] == '*' and dp[i-1][0]

        for i in range(1, len(p)+1):
            for j in range(1, len(s)+1):
                if p[i-1] == '*':
                    dp[i][j] = (
                        dp[i-1][j] or  # Previous pattern match current string.
                        dp[i][j-1]     # Current pattern match previous string.
                    )
                else:
                    dp[i][j] = dp[i-1][j-1] and isCharMatch(s[j-1], p[i-1])

        return dp[len(p)][len(s)]
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def isCharMatch(s, p):
            return p == '.' or s == p

        # dp[i][j]: p[:i] matches s[:j].
        dp = [[False for _ in range(len(s)+1)] for _ in range(len(p)+1)]
        dp[0][0] = True

        # Initialize empty string with all substring of pattern.
        for i in range(2, len(p)+1):
            if p[i-1] == '*' and dp[i-2][0]:
                dp[i][0] = True

        # Fill all cases.
        for i in range(1, len(p)+1):
            for j in range(1, len(s)+1):
                if p[i-1] == '*':
                    dp[i][j] = (
                        # without *, pattern matches whole string.
                        dp[i-2][j] or
                        # with *, pattern matches previous string and * matches the last char.
                        (dp[i][j-1] and isCharMatch(s[j-1], p[i-2]))
                        ) 
                else:
                    dp[i][j] = dp[i-1][j-1] and isCharMatch(s[j-1], p[i-1])

        return dp[len(p)][len(s)]
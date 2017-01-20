class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # # of distinct subsequence with t[:i] and s[:j].
        dp = [[0] * (len(s)+1) for _ in range(len(t)+1)]
        dp[0] = [1] * (len(s)+1)  # Empty t[:i] with all s[:j]. 
        for i in range(1, len(t)+1):
            for j in range(i, len(s)+1):
                dp[i][j] = dp[i][j-1]
                if s[j-1] == t[i-1]:
                    dp[i][j] += dp[i-1][j-1]
        return dp[-1][-1]


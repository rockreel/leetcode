class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Min cut for s[:i]
        dp = [0] * (len(s)+1)
        dp[0] = -1  # For latter s[j:i] if j == 0, can still use +1.
        for i in range(2, len(dp)):
            min_cut = dp[i-1] + 1 # Add one cut for this single letter.
            for j in range(i-2, -1, -1):
                # Find possible smaller cut.
                if s[j:i] == s[j:i][::-1]:
                    min_cut = min(min_cut, dp[j] + 1)
            dp[i] = min_cut
        return dp[-1]


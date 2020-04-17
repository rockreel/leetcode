from typing import List

class Solution:
    def minCut(self, s: str) -> int:
        # dp[i]: min cut number for s[:i]
        dp = [0] * (len(s) + 1)
        dp[0] = -1  # If whole substring s[:j] is a palindrome, then 1 + dp[j] is 0.
        for i in range(2, len(s) + 1):
            mini_cut = i - 1
            for j in range(0, i):
                if s[j:i] == s[j:i][::-1]:
                    mini_cut = min(mini_cut, 1 + dp[j])
            dp[i] = mini_cut
        return dp[-1]
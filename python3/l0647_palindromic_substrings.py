class Solution:
    def countSubstrings(self, s: str) -> int:
        # dp[i][j]: if s[i:j+1] is palindrome
        dp = [[0]*len(s) for _ in s]
        for i in range(len(s)):
            dp[i][i] = 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
            
        for offset in range(2, len(s)):
            for i in range(len(s)-offset):
                if s[i] == s[i+offset] and dp[i+1][i+offset-1] == 1:
                    dp[i][i+offset] = 1
                    
        return sum([sum(r) for r in dp])
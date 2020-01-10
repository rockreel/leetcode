
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_sub = ''
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub = s[i:j+1]
                if sub == sub[::-1] and len(sub) > len(max_sub):
                    max_sub = sub
        return max_sub

    def longestPalindrome2(self, s: str) -> str:
        # dp[i][j]: if s[i:j] is a palindrome.
        dp = [[False for _ in range(len(s)+1)] for _ in range(len(s)+1)]
        max_sub = ''
        for offset in range(len(s)+1):  # offset is substr length
            for i in range(0, len(s)+1-offset):
                j = i + offset
                if offset == 0 or offset == 1:
                    # Length 0 and 1 substring.
                    dp[i][j] = True
                elif s[i] == s[j-1] and dp[i+1][j-1]: 
                    # s[i:j] is palindrome <=> s[i+1:j-1](dp[i+1][j-1]) is palindrome and s[i] == s[j-1]
                    dp[i][j] = True
                if dp[i][j] and offset > len(max_sub):
                        max_sub = s[i:j]
        return max_sub 
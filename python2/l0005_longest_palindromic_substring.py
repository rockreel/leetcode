class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        substr = s[0] if s else ''
        
        # If s[i:j] is palindrome.
        dp = [[False] * (len(s) + 1) for i in range(len(s) + 1)]
        # Initialize 0 and 1 length substring.
        for i in range(len(s) + 1):
            dp[i][i] = True
            dp[i][min(i+1, len(s))] = True

        # Traverse diagonally from 2 length substring and above.
        for offset in range(2, len(s) + 1):
            for i in range(len(s) - offset + 1):
                j = i + offset
                if dp[i+1][j-1] and s[i] == s[j-1]:
                    dp[i][j] = True
                    if j - i > len(substr):
                        substr = s[i:j]

        return substr

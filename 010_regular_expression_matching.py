# DP solution.
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def isMatch(s, p):
            return s == p or p == '.'
        
        # dp[i][j]: if p[:i] matches s[:j]
        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        
        # Empty pattern matches empty string.
        # Empty pattern not match non-empty string.
        # Non-empty pattern only match empty string if it is like a*b*...
        dp[0][0] = True
        for i in range(2, len(p)+1):
            dp[i][0] = dp[i-2][0] if p[i-1] == '*' else False
        
        # For each sub pattern, increase sub string to see if match.
        for i in range(1, len(p)+1):
            for j in range(1, len(s)+1):
                if p[i-1] == '*':
                    dp[i][j] = (
                        # Skip * pattern, p[:i-2] match s[:j]. 
                        dp[i-2][j] or  
                        # Use * pattern, current pattern match up to s[:j-1],
                        # and * can also match last char of s[:j]
                        (dp[i][j-1] and isMatch(s[j-1], p[i-2]))
                    )  
                else:
                    dp[i][j] = dp[i-1][j-1] and isMatch(s[j-1], p[i-1])

        return dp[-1][-1]
        
# Recursive solution.
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) == 0:
            return len(s) == 0
            
        if len(p) > 1 and p[1] == '*':
            if len(s) > 0 and (p[0] == '.' or p[0] == s[0]):
                # Match, either keep using * pattern or skip * pattern.
                return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
            else:
                # Not match skip the * pattern.
                return self.isMatch(s, p[2:])
        else:
            if len(s) > 0 and (p[0] == '.' or p[0] == s[0]):
                return self.isMatch(s[1:], p[1:])
            else:
                return False


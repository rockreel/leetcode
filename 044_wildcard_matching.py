# DP solution.
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """ 
        dp = [
            [None] * (len(s)+1) for _ in range(len(p)+1)
        ]
        
        # Initializae solution matrix.
        dp[0][0] = True  # Empty p match empty s.
        for j in range(1, len(s)+1):
            # Empty p can not match non-empty s.
            dp[0][j] = False
        for i in range(1, len(p)+1):
            # Empty s can still match if current c in p is * and also match previously.
            dp[i][0] = (p[i-1] == '*' and dp[i-1][0])
            
        for i in range(1, len(p)+1):
            for j in range(1, len(s)+1):
                if p[i-1] != '*':
                    dp[i][j] = (p[i-1] == s[j-1] or p[i-1] == '?') and dp[i-1][j-1]
                else:
                    dp[i][j] = (dp[i-1][j] or  # Not-including * already match whole s up to j.
                                dp[i][j-1])     # Including * match s up to j-1.
        return dp[-1][-1]

# Recursive solution.
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """ 
        def wild_card_match(s, p):
            if not p and not s:
                return True

            if not p:
                return False

            if not s:
                return p == '*'

            if s[0] == p[0] or p[0] == '?':
                return wild_card_match(s[1:], p[1:])
            elif p[0] == '*':
                return wild_card_match(s, p[1:]) or wild_card_match(s[1:], p)
            else:
                return False
        
        # Remove multiple *.
        p_trim = []
        for i, c in enumerate(p):
            if c != '*' or i == 0 or p[i-1] != '*':
                p_trim.append(c)
        p = ''.join(p_trim)

        return wild_card_match(s, p)


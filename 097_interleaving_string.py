class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
            
        # If s1[:i], s2[:j] is interleave of s3[:i+j].
        dp = [[False for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
            
        dp[0][0] = True
        for j in range(1, len(s2)+1):
            if s2[j-1] == s3[j-1]:
                dp[0][j]= dp[0][j-1]
                
        for i in range(1, len(s1)+1):
            if s1[i-1] == s3[i-1]:
                dp[i][0] = dp[i-1][0]

        for j in range(1, len(s2)+1):
            for i in range(1, len(s1)+1):
                # True if current letter equal and previously an interleaving.
                if ((s3[i+j-1] == s1[i-1] and dp[i-1][j]) or
                    (s3[i+j-1] == s2[j-1] and dp[i][j-1])):
                    dp[i][j]= True
                        
        return dp[-1][-1]


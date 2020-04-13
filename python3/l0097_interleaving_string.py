class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        # dp[i][j] if s1[:i] and s2[:j] is interleave of s3[:i+j].
        dp = [[False for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        dp[0][0] = True
        for j in range(1, len(s2)+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        for i in range(1, len(s1)+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                dp[i][j] = (
                    (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or
                    (dp[i][j-1] and s2[j-1] == s3[i+j-1])
                )
    
        return dp[-1][-1]

    def isInterleaveRecursive(self, s1: str, s2: str, s3: str) -> bool:
        if not s1 and not s2 and not s3:
            return True

        if not s3 and (not s1 or not s2):
            return False

        if s1 and s1[0] == s3[0]:
            if self.isInterleave(s1[1:], s2, s3[1:]):
                return True

        if s2 and s2[0] == s3[0]:
            if self.isInterleave(s1, s2[1:], s3[1:]):
                return True

        return False
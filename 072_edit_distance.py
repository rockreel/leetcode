class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # Distance between word1[:i] and word2[:j]
        dp = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        
        # Initialize.
        for j in range(len(dp[0])):
            dp[0][j] = j
        for i in range(len(dp)):
            dp[i][0] = i
            
        # Scan.
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] = min(
                    dp[i-1][j] + 1,
                    dp[i][j-1] + 1,
                    dp[i-1][j-1] + (1 if word1[i-1] != word2[j-1] else 0),
                    )
                    
        return dp[-1][-1]


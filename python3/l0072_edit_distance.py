class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp[i][j]: edit distance between word1[:i] and word2[:j]
        dp = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        for i in range(len(word1)+1):
            for j in range(len(word2)+1):
                if i == 0:
                    dp[0][j] = j
                elif j == 0:
                    dp[i][0] = i
                else:
                    dp[i][j] = min(
                        dp[i-1][j-1] if word1[i-1] == word2[j-1] else dp[i-1][j-1] + 1,
                        min(dp[i-1][j]+1, dp[i][j-1]+1)
                    )
        return dp[-1][-1]

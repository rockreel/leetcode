from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid[0]), len(obstacleGrid)
        dp = [[1 - obstacleGrid[i][j] for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    dp[0][j] = dp[0][j-1] if obstacleGrid[0][j] == 0 else 0
                    continue
                if j == 0:
                    dp[i][0] = dp[i-1][0] if obstacleGrid[i][0] == 0 else 0          
                    continue
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
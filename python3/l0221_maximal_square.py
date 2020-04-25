from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dp[i][j]: max square side length with lower right corner at i, j.
        dp = [[0 for _ in matrix[0]] for _ in matrix]
        max_area = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                    continue
                if i == 0 or j == 0:
                    dp[i][j] = 0 if matrix[i][j] == '0' else 1
                else:
                    dp[i][j] = min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1])) + 1
                max_area = max(max_area, dp[i][j] ** 2)
        
        return max_area
                    

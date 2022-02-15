from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # dp[i][j]: minimum fall sum end at i, j.
        dp = [[0] * len(matrix[0]) for _ in matrix]
        dp[0] = matrix[0][:]
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                left_sum = dp[i-1][j-1] if j > 0 else float('inf')
                right_sum = dp[i-1][j+1] if j < len(matrix[0]) - 1 else float('inf')
                middle_sum = dp[i-1][j]
                dp[i][j] = min(left_sum, right_sum, middle_sum) + matrix[i][j]    
        return min(dp[-1])
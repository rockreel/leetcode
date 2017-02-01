class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        # The maximal square length with lower right corner at i, j.
        dp = [[int(c) for c in row] for row in matrix]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        
        return max([max(row) for row in dp]) ** 2


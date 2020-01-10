# O(m^2*n^2) solution
class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        sum_matrix = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix)+1)]
        for i in range(1, len(sum_matrix)):
            for j in range(1, len(sum_matrix[0])):
                sum_matrix[i][j] = matrix[i-1][j-1] + sum_matrix[i][j-1] + sum_matrix[i-1][j] - sum_matrix[i-1][j-1]
        import sys
        max_sum = -sys.maxint
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                for m in range(i, len(matrix)):
                    for n in range(j, len(matrix[0])):
                        # Sum from (i, j) to (m, n).
                        s = sum_matrix[m+1][n+1] - sum_matrix[i][n+1] - sum_matrix[m+1][j] + sum_matrix[i][j]
                        if s <= k:
                            max_sum = max(max_sum, s)
        return max_sum


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        
        # Flip matrix upside down.
        i, j = 0, len(matrix) - 1
        while i < j:
            for k in range(len(matrix[0])):
                matrix[i][k], matrix[j][k] = matrix[j][k], matrix[i][k]
            i += 1
            j -= 1
        
        # Flip matrix diagonally.
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Flip up/down.
        for col in range(len(matrix)):
            row1, row2 = 0, len(matrix) - 1
            while row1 < row2:
                matrix[row1][col], matrix[row2][col] = matrix[row2][col], matrix[row1][col]
                row1 += 1
                row2 -= 1

        # Flip diagonal.
        for row in range(len(matrix)):
            for j in range(row):
                matrix[row][j], matrix[j][row] = matrix[j][row], matrix[row][j]
        
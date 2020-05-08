from typing import List

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self._matrix = matrix
        self._sums = [
            [0] * (len(matrix[0])+1) for  _ in matrix
        ]
        for i in range(len(matrix)):
            sum_ = 0
            for j in range(len(matrix[0])):
                sum_ += matrix[i][j]
                self._sums[i][j+1] = sum_
            

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        diff = val - self._matrix[row][col]
        self._matrix[row][col] = val
        for i in range(col, len(self._matrix[row])):
            self._sums[row][i+1] += diff
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        sum_ = 0
        for i in range(row1, row2+1):
            sum_ += self._sums[i][col2+1] - self._sums[i][col1]
        return sum_


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)

from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            self._sums = [[0]]
            return
        self._sums = [
            [0] * (len(matrix[0])+1) for _ in range(len(matrix)+1)]
        for i in range(1, len(matrix)+1):
            row_sum = 0
            for j in range(1, len(matrix[0])+1):
                row_sum += matrix[i-1][j-1]
                self._sums[i][j] = self._sums[i-1][j] + row_sum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self._sums[row2+1][col2+1] - self._sums[row1][col2+1] -
            self._sums[row2+1][col1] + self._sums[row1][col1]
        )

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

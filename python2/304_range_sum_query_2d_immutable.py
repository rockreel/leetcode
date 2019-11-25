class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self._sum = [[0] * (len(matrix[0] if matrix else [])+1) for _ in range(len(matrix)+1)]
        for i in range(1, len(matrix)+1):
            row_sum = 0
            for j in range(1, len(matrix[0])+1):
                row_sum += matrix[i-1][j-1]
                self._sum[i][j] = self._sum[i-1][j] + row_sum
                
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return (
            self._sum[row2+1][col2+1] + self._sum[row1][col1] -
            self._sum[row1][col2+1] - self._sum[row2+1][col1]
            )
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


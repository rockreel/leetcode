class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        
        # Check first row/col.
        first_row_zero = False
        for c in matrix[0]:
            if c == 0:
                first_row_zero = True
        first_col_zero = False    
        for r in matrix:
            if r[0] == 0:
                first_col_zero = True
                
        # Scan and mark on first row/col.
        for i, row in enumerate(matrix):
            for j, c in enumerate(row):
                if c == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        # Set zeros.
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        if first_row_zero:
           for j in range(len(matrix[0])):
               matrix[0][j] = 0
        if first_col_zero:
            for i in range(len(matrix)):
               matrix[i][0] = 0
               
        return


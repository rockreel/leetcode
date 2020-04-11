from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        # Binary search to decide which row the target is.
        row_start, row_end = 0, len(matrix) - 1
        while row_start < row_end - 1:
            row_middle = (row_start + row_end) // 2
            if matrix[row_middle][0] > target:
                row_end = row_middle - 1
            elif matrix[row_middle][0] <= target:
                row_start = row_middle

        if target >= matrix[row_end][0]:
            row = row_end
        else:
            row = row_start

        # Binary search on the row indentified preivously.
        col_start, col_end = 0, len(matrix[0]) - 1
        while col_start <= col_end:
            col_middle = (col_start + col_end) // 2
            if matrix[row][col_middle] > target:
                col_end = col_middle - 1
            elif matrix[row][col_middle] < target:
                col_start= col_middle + 1
            else:
                return True
        
        return False
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
            
        # Binary search the row.
        start, end = 0, len(matrix) - 1
        row = -1
        while start <= end:
            middle = (start + end) / 2
            if (matrix[middle][0] <= target and
                matrix[middle][-1] >= target):
                row = middle
                break
            elif matrix[middle][0] > target:
                end = middle - 1
            else:  # matrix[middle][-1] < target
                start = middle + 1
        else:
            return False
        
        # Binary search within a row.
        start, end = 0, len(matrix[0]) - 1
        while start <= end:
            middle = (start + end) / 2
            if matrix[row][middle] == target:
                return True
            elif matrix[row][middle] > target:
                end = middle - 1
            else:
                start = middle + 1
        return False


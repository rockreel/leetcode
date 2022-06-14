from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        left_bound, right_bound = 0, len(matrix[0]) - 1
        up_bound, down_bound = 0, len(matrix) - 1
        result = []
        while left_bound < right_bound and up_bound < down_bound:
            for i in range(left_bound, right_bound+1):
                result.append(matrix[up_bound][i])
            for i in range(up_bound+1, down_bound+1):
                result.append(matrix[i][right_bound])
            for i in range(right_bound-1, left_bound-1, -1):
                result.append(matrix[down_bound][i])
            for i in range(down_bound-1, up_bound, -1):
                result.append(matrix[i][left_bound])
            left_bound += 1
            right_bound -= 1
            up_bound += 1
            down_bound -= 1
        if up_bound == down_bound:
            for i in range(left_bound, right_bound+1):
                result.append(matrix[up_bound][i])
        elif left_bound == right_bound:
            # In case there is only one left at center, "elif" will have it covered
            # in previous "if" clause.
            for i in range(up_bound, down_bound+1):
                result.append(matrix[i][right_bound])   
        return result

    def spiralOrder2(self, matrix: List[List[int]]) -> List[int]:
        offset = 0
        m = len(matrix)
        n = len(matrix[0])
        result = []
        while offset < m // 2 and offset < n // 2:
            for j in range(offset, n-offset-1):
                result.append(matrix[offset][j])
            for i in range(offset, m-offset-1):
                result.append(matrix[i][n-offset-1])
            for j in range(n-offset-1, offset, -1):
                result.append(matrix[m-offset-1][j])
            for i in range(m-offset-1, offset, -1):
                result.append(matrix[i][offset])
            offset += 1
        if n >= m:
            if m % 2 == 1:
                for j in range(offset, n - offset):
                    result.append(matrix[offset][j])
        else:
            if n % 2 == 1:
                for i in range(offset, m - offset):
                    result.append(matrix[i][offset])
        return result
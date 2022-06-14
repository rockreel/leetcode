from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0:
            return []
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        i, j = 0, 0
        direction = 'R'
        for num in range(1, n*n+1):
            matrix[i][j] = num
            if direction == 'R':
                if j + 1 <= n - 1 and matrix[i][j+1] == 0:
                    j += 1
                else:
                    direction = 'D'
                    i += 1
            elif direction == 'D':
                if i + 1 <= n - 1 and matrix[i+1][j] == 0:
                    i += 1
                else:
                    direction = 'L'
                    j -= 1
            elif direction == 'L':
                if j - 1 >= 0 and matrix[i][j-1] == 0:
                    j -= 1
                else:
                    direction = 'U'
                    i -= 1
            else:
                if i - 1 >= 0 and matrix[i-1][j] == 0:
                    i -= 1
                else:
                    direction = 'R'
                    j += 1
        return matrix

    def generateMatrix4Loops(self, n: int) -> List[List[int]]:
        num = 1
        matrix = [[0] * n for _ in range(n)]
        offset = 0
        i_start, j_start = 0, 0
        while offset < n // 2:
            for j in range(j_start, n - offset - 1):
                matrix[i_start][j] = num
                num += 1
            for i in range(i_start, n - offset - 1):
                matrix[i][n - offset - 1] = num
                num += 1
            for j in range(n - offset - 1, offset, -1):
                matrix[n - offset - 1][j] = num
                num += 1
            for i in range(n - offset - 1, offset, -1):
                matrix[i][offset] = num
                num += 1
            i_start += 1
            j_start += 1
            offset += 1
        if n % 2 == 1:
            matrix[n//2][n//2] = num
        return matrix
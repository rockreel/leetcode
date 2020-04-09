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

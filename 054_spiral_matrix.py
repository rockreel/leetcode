class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        direction = 'r'
        result = []
        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0
        while len(result) < m * n:
            result.append(matrix[i][j])
            matrix[i][j] = 'x'
            
            if direction == 'r':
                if j == n - 1 or matrix[i][j+1] == 'x':
                    direction = 'd'
                    i += 1
                else:
                    j += 1
            elif direction == 'd':
                if i == m - 1 or matrix[i+1][j] == 'x':
                    direction = 'l'
                    j -= 1
                else:
                    i += 1
            elif direction == 'l':
                if j == 0 or matrix[i][j-1] == 'x':
                    direction = 'u'
                    i -= 1
                else:
                    j -= 1
            else:
                if i == 0 or matrix[i-1][j] == 'x':
                    direction = 'r'
                    j += 1
                else:
                    i -= 1
            
        return result


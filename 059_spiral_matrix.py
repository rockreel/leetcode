class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [['' for _ in range(n)] for _ in range(n)]
        i, j = 0, 0
        direction = 'r'
        num = 1
        while num < n * n + 1:
            matrix[i][j] = num
            num += 1
            if direction == 'r':
                if j == n - 1 or matrix[i][j+1] != '':
                    direction = 'd'
                    i += 1
                else:
                    j += 1
            elif direction == 'd':
                if i == n - 1 or matrix[i+1][j] != '':
                    direction = 'l'
                    j -= 1
                else:
                    i += 1
            elif direction == 'l':
                if j == 0 or matrix[i][j-1] != '':
                    direction = 'u'
                    i -= 1
                else:
                    j -= 1
            elif direction == 'u':
                if i == 0 or matrix[i-1][j] != '':
                    direction = 'r'
                    j += 1
                else:
                    i -= 1
        return matrix


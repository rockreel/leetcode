class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
            
        triangle = [[1]]
        for n in range(1, numRows):
            triangle.append([])
            for i in range(n+1):
                if i == 0 or i == n:
                    triangle[n].append(1)
                else:
                    triangle[n].append(triangle[n-1][i-1]+triangle[n-1][i])

        return triangle


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        # Min # of squares summed up to i.
        num_squares = [0] * (n + 1)
        for i in range(1, n+1):
            min_square = i
            for j in range(1, int(math.sqrt(i))+1):
                min_square = min(num_squares[i-j*j], min_square)
            num_squares[i] = min_square + 1
        return num_squares[-1]


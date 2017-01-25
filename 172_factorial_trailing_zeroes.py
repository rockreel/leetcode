class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        num_zeros = 0
        while n / 5**i > 0:
            num_zeros += n / 5**i
            i += 1
        return num_zeros


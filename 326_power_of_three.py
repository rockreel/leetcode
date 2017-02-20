class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 0 and n % 3 == 0:
            n /= 3
        return n == 1


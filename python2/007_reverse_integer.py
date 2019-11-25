class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        n = abs(x)
        r = 0
        while n > 0:
            r = r * 10 + n % 10
            if r > 2 ** 31:
                return 0
            n = n / 10
        return sign * r
        


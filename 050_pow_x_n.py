class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        
        positive_pow = True
        if n < 0:
            positive_pow = False
            n = -n
        
        result = 1
        while n > 0:
            power = 1
            inter_result = x
            while 2 * power <= n:
                inter_result = inter_result * inter_result
                power = 2 * power
            result = result * inter_result
            n = n - power
        
        if positive_pow:
            return result
        else:
            return 1 / result


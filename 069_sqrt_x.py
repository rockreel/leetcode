class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = 0
        up = x
        r = (up + low) / 2
        while not ((r + 1)**2 > x and r**2 <= x):
            if r**2 > x:
                up = r
            elif (r+1)**2 <= x:
                low = r + 1
            r = (up + low) / 2 
        return r


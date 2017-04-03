class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low, up = 0, x
        r = (low + up) / 2
        # Stop if r**2 <= x and (r+1)**2 > x
        while not ((r+1)**2 > x and r**2 <= x):
            if (r+1)**2 <= x:
                low = r + 1
            else:
                up = r - 1
            r = (low + up) / 2
        return r


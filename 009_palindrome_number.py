class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        n = abs(x)
        r = 0
        while n > 0:
            r = 10 * r + n % 10
            n /= 10
        return r == x
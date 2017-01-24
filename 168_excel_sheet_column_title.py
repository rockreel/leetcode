class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        title = ''
        while n:
            title = chr((n-1)%26+65) + title
            n = (n-1)/26
        return title


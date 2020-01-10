class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0]
        for n in range(1, num+1):
            if n & (n-1) == 0: # n is power of 2.
                i = 0
            result.append(1+result[i])
            i += 1
        return result


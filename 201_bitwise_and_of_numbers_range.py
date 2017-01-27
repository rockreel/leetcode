class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # Find most significant bits.
        msb_m = 0
        m0 = m
        while m0 > 0:
            m0 = m0 >> 1
            msb_m += 1
        msb_n = 0
        n0 = n
        while n0 > 0:
            n0 = n0 >> 1
            msb_n += 1
        
        if msb_m != msb_n or msb_m == 0:
            return 0
        
        # Find the range of both have same bits since most significant bit.
        # That should be the result.
        result = 0
        mask = (1 << (msb_m - 1))
        while mask and mask & m == mask & n:
            result += mask & m
            mask = mask >> 1
            
        return result


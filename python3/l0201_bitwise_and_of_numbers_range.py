class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        # Find most significant bits.
        m0 = m
        msb_m = 0
        while m0 > 0:
            m0 = m0 >> 1
            msb_m += 1
        n0 = n
        msb_n = 0
        while n0 > 0:
            n0 = n0 >> 1
            msb_n += 1

        # If most significant bits are different, then 0.
        if msb_n != msb_m or msb_m == 0:
            return 0

        # If most significant bits are same, find most significant bits
        # porttion that are same.
        mask = 1 << (msb_m - 1)
        result = 0
        while mask > 0 and (m & mask) == (n & mask):
            result += mask & m
            mask = mask >> 1
        return result
            

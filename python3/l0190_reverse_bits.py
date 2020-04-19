class Solution:
    def reverseBits(self, n: int) -> int:
        r = 0
        i = 0
        while i < 32:
            b = n & 1
            r = (r << 1) + b
            n = n >> 1
            i += 1
        return r

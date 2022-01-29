class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        d = 0
        while xor > 0:
            d += xor & 1
            xor = xor >> 1
        return d
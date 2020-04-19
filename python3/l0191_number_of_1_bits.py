ass Solution:
    def hammingWeight(self, n: int) -> int:
        w = 0
        while n > 0:
            w += n & 1
            n = n >> 1
        return w

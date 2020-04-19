class Solution:
    def trailingZeroes(self, n: int) -> int:
        num = 0
        i = 1
        while 5 ** i <= n:
            num += (n // (5 ** i))
            i += 1
        return num


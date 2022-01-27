class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        i = 1
        while n % (3 ** i) == 0:
            i = i * 2
        if i == 1:
            return False

        return self.isPowerOfThree(n // (3 ** (i // 2)))


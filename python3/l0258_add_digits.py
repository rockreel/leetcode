class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            r = 0
            while num > 0:
                r += num % 10
                num //= 10
            num = r
        return num

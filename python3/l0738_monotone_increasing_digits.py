class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = []
        while n > 0:
            digits.insert(0, n % 10)
            n = n // 10
        index_nine = len(digits)
        for i in range(len(digits)-1, 0, -1):
            if  digits[i] < digits[i-1]:
                digits[i-1] = digits[i-1] - 1
                digits[i] = 9
                index_nine = i
        for i in range(index_nine+1, len(digits)):
            digits[i] = 9
        result = 0
        for d in digits:
            result = 10 * result + d
        return result
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative = (
          (dividend > 0 and divisor < 0) or 
          (dividend < 0 and divisor > 0)
        )
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        while dividend >= divisor:
            temp_divisor, multiplier = divisor, 1
            while dividend >= temp_divisor:
                dividend -= temp_divisor
                quotient += multiplier
                # Double temp divisor and multiplier each iteration,
                # until updated dividend is less then this temp divisor.
                temp_divisor <<= 1
                multiplier <<=1

        if negative:
            quotient = -quotient

        return min(quotient, 2**31-1)
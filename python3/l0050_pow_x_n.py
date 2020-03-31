import decimal

class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        negative = False
        if n < 0:
            negative = True
            n = -n
            
        while n > 0:
            power = 1
            base = x
            while power <= n:
                if negative:
                    result /= base
                else:
                    result *= base
                n -= power
                power *= 2
                base = base ** 2

        return result

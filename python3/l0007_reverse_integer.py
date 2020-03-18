class Solution:
  
    def reverse(self, x: int) -> int:
        r = 0
        sign = 1
        if x < 0:
            sign = -1
            x = -x 
        while x > 0:
            r = r * 10 + x % 10
            x = x // 10
            if (r > 2 ** 31 - 1 and sign == 1) or (r > 2 ** 31 and sign == -1):
                return 0
        return sign * r
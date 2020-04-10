class Solution:
    def mySqrt(self, x: int) -> int:
        up = x
        low = 1
        r = (up + low) // 2
        while not (r ** 2 <= x and (r + 1) ** 2 > x):
            if (r + 1) ** 2 <= x :
                low = r + 1
            else:
                up = r - 1
            r = (up + low) // 2
        return r
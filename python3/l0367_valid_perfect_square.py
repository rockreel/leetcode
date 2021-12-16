class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start, end = 0, num
        while start <= end:
            m = start + (end - start) // 2
            if m * m == num:
                return True
            elif m * m < num:
                start = m + 1
            else:
                end = m - 1
        return False
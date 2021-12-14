# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:



class Solution:

    def __init__(self, pick):
        self.pick = pick

    def guess(self, n):
        if n == self.pick:
            return 0
        if n > self.pick:
            return -1
        return 1

    def guessNumber(self, n: int) -> int:
        start, end = 1, n
        while start <= end:
            middle = (start + end) // 2
            r = self.guess(middle)
            if r == 0:
                return middle
            elif r > 0:
                start = middle + 1
            else:
                end = middle - 1
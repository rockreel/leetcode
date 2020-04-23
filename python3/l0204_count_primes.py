class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        nums = [0] * n
        nums[:2] = [1, 1]
        i = 2
        while i < n:
            while i < n and nums[i] != 0:
                i += 1
            j = 2
            while j * i < n:
                nums[i*j] = 1
                j += 1
            i += 1
        return len([n for n in nums if n == 0])

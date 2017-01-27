class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        nums = range(n)
        nums[:2] = [0, 0]
        i = 2
        while i < math.sqrt(n):
            if nums[i] != 0:
                j = nums[i]
                while j*nums[i] < n:
                    nums[j*nums[i]] = 0
                    j += 1
            i += 1
        return len([n for n in nums if n != 0])


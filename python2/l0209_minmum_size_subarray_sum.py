class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        min_len = None
        i, j, sum = 0, 0, 0
        while i < len(nums):
            sum += nums[i]
            if sum >= s:
                while sum >= s:
                    if min_len is None:
                        min_len = i-j+1
                    else:
                        min_len = min(min_len, i-j+1)
                    sum -= nums[j]
                    j += 1
            i += 1

        return 0 if min_len is None else min_len


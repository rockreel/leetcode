class Solution:
    """
    @param nums: a list of integer
    @return: return a integer, denote  the maximum number of consecutive 1s
    """
    def findMaxConsecutiveOnes(self, nums):
        curr_len = 0
        max_len = 0
        start = -1
        flip = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                curr_len = i - start
                max_len = max(curr_len, max_len)
            else:
                if flip != -1:
                    start = flip
                flip = i
        return max_len
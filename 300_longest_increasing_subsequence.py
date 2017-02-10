# O(n^2) solution.
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        # Longest sub sequence length starts at i.
        longest_length = [0] * len(nums)
        longest_length[-1] = 1
        for i in range(len(nums)-2, -1, -1):
            max_len = 1
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    max_len = max(max_len, 1+longest_length[j])
            longest_length[i] = max_len
        return max(longest_length)


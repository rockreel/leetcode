class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Max money can get from nums[:i-1] houses.
        dp = [0] * (len(nums) + 2)
        for i in range(2, len(nums)+2):
            dp[i] = max(nums[i-2] + dp[i-2], dp[i-1])
        return dp[-1]


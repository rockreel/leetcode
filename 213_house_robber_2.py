class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
            
        if len(nums) <= 2:
            return max(nums)
            
        # Last house is not included.
        dp = [0] * (len(nums) - 1)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)-1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        max_money = dp[-1]
        
        # First house is not included.
        dp = [0] * (len(nums) - 1)
        dp[0] = nums[1]
        dp[1] = max(nums[1], nums[2])
        for i in range(2, len(nums)-1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i+1])
            
        return max(max_money, dp[-1])


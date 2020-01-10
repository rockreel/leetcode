class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        # Max points on sub list of nums[i:j+1].
        dp = [[0] * len(nums) for _ in nums]
        nums = [1] + nums + [1]
        for i in range(len(dp)):
            dp[i][i] = nums[i]*nums[i+1]*nums[i+2]
            
        for j in range(1, len(dp)):  # Off diagonal by j.
            for i in range(len(dp)-j):  # Find max points for nums[i:i+j+1].
                max_coin = 0
                for k in range(i, i+j+1):  # Last burst balloon is nums[k].
                    left_coin = dp[i][k-1] if i<=k-1 else 0
                    right_coin = dp[k+1][i+j] if k+1<=i+j else 0
                    max_coin = max(
                        max_coin,
                        nums[i]*nums[k+1]*nums[i+j+2] + left_coin + right_coin)
                dp[i][i+j] = max_coin

        return dp[0][-1]


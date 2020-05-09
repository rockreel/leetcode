from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # dp[i][j]: max coins burst nums[i:j+1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        nums = [1] + nums + [1]
        for offset in range(n):
            for i in range(n-offset):
                j = i + offset
                if offset == 0:
                    # nums has 1 at front and end.
                    dp[i][j] = nums[i] * nums[i+1] * nums[i+2]
                else:
                    for k in range(i, j+1):
                        left_coin = dp[i][k-1] if k - 1 >= i else 0
                        right_coin = dp[k+1][j] if k + 1 <= j else 0
                        dp[i][j] = max(
                            dp[i][j],
                            # nums has 1 at front and end.
                            nums[i] * nums[k+1] * nums[j+2] + left_coin + right_coin
                        )
        return dp[0][-1]

    def maxCoinsRecursive(self, nums: List[int]) -> int:
        def max_coins(nums: List[int]) -> int:
            if len(nums) == 3:
                return nums[0] * nums[1] * nums[2]
            max_point = 0
            for i in range(1, len(nums)-1):
                max_point = max(
                    max_point,
                    nums[i] * nums[i-1] * nums[i+1] + 
                    max_coins(nums[:i] + nums[i+1:]))
            return max_point
        return max_coins([1] + nums + [1])


from typing import List

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # dp[i][j]: i'th step, left position of nums is j.
        dp = [[0] * (len(multipliers) + 1) for _ in range(len(multipliers) + 1)]
        for i in range(len(dp)-2, -1, -1):
            for left in range(i, -1, -1):
                right = len(nums) - 1 - (i - left)
                dp[i][left] = max(
                    dp[i+1][left+1] + nums[left] * multipliers[i],
                    dp[i+1][left] + nums[right] * multipliers[i]
                )
        return dp[0][0]

    def maximumScoreCache(self, nums: List[int], multipliers: List[int]) -> int:
        def maxScore(nums, multipliers, i, left, cache):
            if i == len(multipliers):
                return 0
            if (i, left) in cache:
                return cache[(i, left)]
            right = len(nums) - 1 - (i - left)
            m = multipliers[i]
            result = max(
                maxScore(nums, multipliers, i + 1, left + 1, cache) + nums[left] * m,
                maxScore(nums, multipliers, i + 1, left, cache) + nums[right] * m,
            )
            cache[(i, left)] = result
            return result
        return maxScore(nums, multipliers, 0, 0, {})

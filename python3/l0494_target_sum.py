from typing import List

class Solution:

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        result_cache = {}
        def calculate(nums, i, target):
            nonlocal result_cache
            if i == len(nums):
                if target == 0:
                    result_cache[(i, target)] = 1
                    return 1
                else:
                    result_cache[(i, target)] = 0
                    return 0
            
            if (i, target) in result_cache:
                return result_cache[(i, target)]
            
            result = 0
            result += calculate(nums, i+1, target - nums[i])
            result += calculate(nums, i+1, target + nums[i])
            result_cache[(i, target)] = result
            return result
        
        return calculate(nums, 0, target)

    def findTargetSumWaysDP2D(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        dp = [[0] * (s * 2 + 1) for _ in range(len(nums))]
        dp[0][s+nums[0]] = 1
        dp[0][s-nums[0]] += 1
        for i in range(1, len(dp)):
            for j in range(len(dp[0])):
                if dp[i-1][j] > 0:
                    dp[i][j-nums[i]] = dp[i-1][j] + dp[i][j-nums[i]]
                    dp[i][j+nums[i]] = dp[i-1][j] + dp[i][j+nums[i]]
        return dp[-1][s+target] if target <= s else 0

    def findTargetSumWaysDP1D(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        dp = [0] * (s * 2 + 1)
        dp[s+nums[0]] = 1
        dp[s-nums[0]] += 1
        print(dp)
        for i in range(1, len(nums)):
            dp_next = [0] * (s * 2 + 1)
            for j in range(len(dp)):
                if dp[j] > 0:
                    dp_next[j-nums[i]] = dp[j] + dp_next[j-nums[i]]
                    dp_next[j+nums[i]] = dp[j] + dp_next[j+nums[i]]
            dp = dp_next
            print(dp)
            
        return dp[s+target] if target <= s else 0

    def findTargetSumWaysKnapsack(self, nums: List[int], target: int) -> int:
        # A + B = sum(nums)
        # A - B = target
        # => A = (sum(nums) + target) // 2
        target = sum(nums) + target
        if target % 2 != 0:
            return 0
        target = target // 2
        if target < 0:
            return 0
        dp = [[0] * (target + 1) for _ in nums]
        
        for i in range(len(dp)):
            dp[i][0] = 1
        for j in range(len(dp[0])):
            if nums[0] == j:
                dp[0][j] += 1

        for i in range(1, len(dp)):
            for j in range(0, len(dp[0])):
                dp[i][j] = dp[i-1][j] + (dp[i-1][j-nums[i]] if j -nums[i] >= 0 else 0)

        return dp[-1][-1]
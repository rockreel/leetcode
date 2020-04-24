from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        if len(nums) <= 2:
            return max(nums)
        # Rob the first house.
        money0 = [0] * len(nums)
        money0[:2] = [nums[0], nums[0]]
        for i in range(2, len(nums) - 1):
            money0[i] = max(nums[i] + money0[i-2], money0[i-1])
        
        # Rob the second house.
        money1 = [0] * len(nums)
        money1[1] = nums[1]
        for i in range(2, len(nums)):
            money1[i] = max(nums[i] + money1[i-2], money1[i-1])

        return max(money0[-2], money1[-1])


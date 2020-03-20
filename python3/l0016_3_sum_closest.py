from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        def twoSumClosestSorted(nums: List[int], target: int) -> int:
            i, j = 0, len(nums) - 1
            diff = float('inf')
            while i < j:
                if abs(diff) >  abs(target - (nums[i] + nums[j])):
                    diff = target - (nums[i] + nums[j])
                if nums[i] + nums[j] < target:
                    i += 1
                elif nums[i] + nums[j] > target:
                    j -= 1
                else:
                    return 0
            return diff
        
        nums = sorted(nums)
        min_diff = float('inf')
        for i, n in enumerate(nums):
            diff = twoSumClosestSorted(nums[i+1:], target - n)
            if abs(min_diff) > abs(diff):
                min_diff = diff
        return target - min_diff
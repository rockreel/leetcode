from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def twoSumSorted(nums: List[int], target: int) -> List[List[int]]:
            i, j = 0, len(nums) - 1
            result = set()
            while i < j:
                if nums[i] + nums[j] < target:
                    i += 1
                elif nums[i] + nums[j] > target:
                    j -= 1
                else:
                    result.add((nums[i], nums[j]))
                    i += 1
                    j -= 1
            return result
        
        def threeSumSorted(nums: List[int], target: int) -> List[List[int]]:
            result = set()
            for i, n in enumerate(nums):
                for r in twoSumSorted(nums[i+1:], target - n):
                    result.add((n, r[0], r[1]))
            return result
        
        nums = sorted(nums)
        result = set()
        for i, n in enumerate(nums):
            for r in threeSumSorted(nums[i+1:], target - n):
                result.add((n, r[0], r[1], r[2]))
        return [[r[0], r[1], r[2], r[3]] for r in result]
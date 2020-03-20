from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSumSorted(nums: List[int], target) -> List[List[int]]:
            i, j = 0, len(nums) - 1
            result = []
            while i < j:
                if nums[i] + nums[j] < target:
                    i += 1
                elif nums[i] + nums[j] > target:
                    j -= 1
                else:
                    result.append((nums[i], nums[j]))
                    i += 1
                    j -= 1
            return result
        
        nums = sorted(nums)
        result = set()
        for i, n in enumerate(nums):
            for r in twoSumSorted(nums[i+1:], -n):
                result.add((n, r[0], r[1]))
        return [[r[0], r[1], r[2]] for r in result]

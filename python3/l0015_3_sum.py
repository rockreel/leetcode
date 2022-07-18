from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        i = 0
        while i < len(nums) - 2:
            target = - nums[i]
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[j] + nums[k] == target:
                    result.append([nums[i], nums[j], nums[k]])
                    while k - 1 >= 0 and nums[k] == nums[k-1]:
                        k -= 1
                    k -= 1
                    while j + 1 < len(nums) and nums[j+1] == nums[j]:
                        j += 1
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    j += 1
            while i + 1 < len(nums) - 2 and nums[i+1] == nums[i]:
                i += 1
            i += 1
        return result

    def threeSumWithSet(self, nums: List[int]) -> List[List[int]]:
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

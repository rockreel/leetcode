from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        result = []
        for i, n in enumerate(nums):
            for r in self.permute(nums[:i] + nums[i+1:]):
                result.append([n] + r)
        return result

    def permuteIndex(self, nums: List[int]) -> List[List[int]]:
        def find_permutation(nums, perm, result, used):
            if len(perm) == len(nums):
                result.append(perm)
                return
            for i in range(len(nums)):
                if nums[i] in used:
                    continue
                used.add(nums[i])
                find_permutation(nums, perm + [nums[i]], result, used)
                used.remove(nums[i])
                
            return result
        result = []
        find_permutation(nums, [], result, set([]))
        return result
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def permuteUniqueImpl(nums: List[int]) -> List[List[int]]:
            if len(nums) == 1:
                return [nums]
            prev = None
            result = []
            for i, n in enumerate(nums):
                if n == prev:
                    continue
                for r in self.permuteUnique(nums[:i] + nums[i+1:]):
                    result.append([n] + r)
                prev = n
            return result
        return permuteUniqueImpl(sorted(nums))

    def permuteUniqueIndex(self, nums: List[int]) -> List[List[int]]:
        def find_permutation(nums, perm, result, used_on_branch):
            if len(perm) == len(nums):
                result.append(perm)
                return
            used_on_level = set([])
            for i in range(len(nums)):
                if nums[i] in used_on_level:
                    continue
                if i in used_on_branch:
                    continue
                used_on_level.add(nums[i])
                used_on_branch.add(i)
                find_permutation(nums, perm + [nums[i]], result, used_on_branch)
                used_on_branch.remove(i)
                
            return result
        result = []
        find_permutation(sorted(nums), [], result, set([]))
        return result
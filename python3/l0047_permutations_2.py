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
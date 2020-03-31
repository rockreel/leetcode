from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        result = []
        for i, n in enumerate(nums):
            for r in self.permute(nums[:i] + nums[i+1:]):
                result.append([nums[i]] + r)
        return result
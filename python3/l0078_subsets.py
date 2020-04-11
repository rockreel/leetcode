from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        subsets = []
        for s in self.subsets(nums[1:]):
            subsets.append(s)
            subsets.append([nums[0]] + s)
        return subsets
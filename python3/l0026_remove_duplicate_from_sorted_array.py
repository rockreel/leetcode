from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        f, b = 1, 0
        while f < len(nums):
            if nums[f] != nums[b]:
                nums[f], nums[b+1] = nums[b+1], nums[f]
                b += 1
            f += 1
        return b + 1
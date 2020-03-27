from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        b, f = -1, 0
        while f < len(nums):
            if nums[f] != val:
                nums[f], nums[b+1] = nums[b+1], nums[f]
                b += 1
            f += 1
        return b + 1
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0, p2, p = -1, len(nums), 0  # p0 points to last 0; p2 points to first 2
        while p < p2:
            if nums[p] == 0:
                nums[p0+1], nums[p] = nums[p], nums[p0+1]
                p0 += 1
            elif nums[p] == 2:
                nums[p2-1], nums[p] = nums[p], nums[p2-1]
                p2 -= 1
            else:
                p += 1
            p = max(p, p0+1)

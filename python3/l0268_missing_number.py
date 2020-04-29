from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        found_nums = [0] * (len(nums) + 1)
        for n in nums:
            found_nums[n] = 1
        return found_nums.index(0)
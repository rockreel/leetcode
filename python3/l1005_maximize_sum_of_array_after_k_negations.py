from typing import List

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        i = 0
        while i < len(nums) and nums[i] < 0 and i < k:
            nums[i] = - nums[i]
            i += 1
        k = max(0, k - i)
        if k % 2 == 0:
            return sum(nums)
        else:
            nums = sorted(nums)
            return sum(nums) - 2 * nums[0]
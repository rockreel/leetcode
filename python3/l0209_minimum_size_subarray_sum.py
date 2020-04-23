from typing import List

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        i, j = 0, 0
        sum_ = 0
        min_len = len(nums) + 1
        while j < len(nums):
            while j < len(nums) and sum_ < s:
                sum_ += nums[j]
                j += 1
            while i <= j and sum_ >= s:
                min_len = min(min_len, j - i)
                sum_ -= nums[i]
                i += 1
        return min_len if min_len != len(nums) + 1 else 0
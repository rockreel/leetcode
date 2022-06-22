from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        pre_diff = 0
        curr_diff = 0
        result = 1
        for i in range(len(nums)-1):
            curr_diff = nums[i+1] - nums[i]
            if (curr_diff > 0 and pre_diff <= 0) or (curr_diff < 0 and pre_diff >= 0):
                result += 1
                pre_diff = curr_diff
        return result

from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(sum(nums), max(nums))
        
        # Calculate 1 interval sub-array (regular).
        max_sum_1_interval = float('-inf')
        s = 0
        for n in nums:
            s += n
            max_sum_1_interval = max(max_sum_1_interval, s)
            if s < 0:
                s = 0
                
        # Calculate 2 interval sub-array, i.e. subarray connected from end to begining.
        # Sum of all elements from left to i.
        sum_from_left = [0] * len(nums)
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            sum_from_left[i] = s

        # Max sum from right up to i.
        max_sum_from_right = [0] * len(nums)
        max_sum = float('-inf')
        sum_from_right = 0
        for i in range(len(nums)-1, -1, -1):
            sum_from_right += nums[i]
            max_sum = max(max_sum, sum_from_right)
            max_sum_from_right[i] = max_sum
                
        max_sum_2_interval = float('-inf')
        for i in range(len(nums)-2):
            max_sum_2_interval = max(max_sum_2_interval, sum_from_left[i] + max_sum_from_right[i + 2])
            
        return max(max_sum_1_interval, max_sum_2_interval)
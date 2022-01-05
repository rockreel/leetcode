from typing import List

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def check(nums, m, s):
            if not nums:
                return False
            if max(nums) > s:
                return False
            count = 1
            curr_sum = nums[0]
            for n in nums[1:]:
                curr_sum += n
                if curr_sum > s:
                    count += 1
                    curr_sum = n
            return count <= m
        
        start, end = 0, sum(nums)
        while start < end:
            middle = start + (end - start) // 2
            if check(nums, m, middle):
                end = middle
            else:
                start = middle + 1
        return start

    def splitArraySlow(self, nums: List[int], m: int) -> int:
        if m == 1:
            return sum(nums)
        min_sum = float('inf')
        curr_sum = 0
        for i in range(len(nums) - m + 1):
            curr_sum += nums[i]
            min_sum = min(min_sum, max(curr_sum, self.splitArray(nums[i+1:], m-1)))
        return min_sum
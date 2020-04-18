from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1      
        while start + 1 < end:
            if nums[start] < nums[end]:
                return nums[start]
            middle = (start + end) // 2
            if nums[middle] > nums[start]:
                start = middle
            elif nums[middle] < nums[end]:
                end = middle
            else:
                if nums[middle] == nums[start]:
                    start += 1
                if nums[middle] == nums[end]:
                    end -= 1     
        return min(nums[start], nums[end])
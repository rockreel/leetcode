from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            middle = (start + end) // 2
            left = nums[middle - 1] if middle - 1 >= 0 else float('-inf')
            right = nums[middle + 1] if middle + 1 < len(nums) else float('-inf')
            if nums[middle] > left and nums[middle] > right:
                return middle
            elif nums[middle] < left:
                end = middle
            else:
                start = middle
        return start if nums[start] > nums[end] else end
        

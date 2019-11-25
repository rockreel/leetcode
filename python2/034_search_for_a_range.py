class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
            
        # Search for lower bound.
        start, end = 0, len(nums) - 1
        while start < end:
            middle = (start + end) / 2
            if nums[middle] >= target:
                end = middle
            else:
                start = middle + 1
        lower_bound = start if nums[start] == target else -1
        
        # Search for upper bound.
        start, end = 0, len(nums) - 1
        while start < end:
            middle = (start + end) / 2 + 1
            if nums[middle] <= target:
                start = middle
            else:
                end = middle - 1
        upper_bound = start if nums[start] == target else -1
        
        return [lower_bound, upper_bound]

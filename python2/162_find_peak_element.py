class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums)-1
        while start < end - 1:    
            middle = (start + end)/2
            if nums[middle] > nums[middle-1] and nums[middle] > nums[middle+1]:
                return middle
            elif nums[middle] <= nums[middle-1]:
                end = middle - 1
            else:
                start = middle + 1
        return start if nums[start] >= nums[end] else end


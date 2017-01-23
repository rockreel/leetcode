class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums)-1
        
        if nums[start] < nums[end]:  # No rotation.
            return nums[start]
            
        while start < end - 1:
            middle = (start+end)/2
            if nums[middle] > nums[start]:
                start = middle
            elif nums[middle] < nums[end]:
                end = middle
                
        return min(nums[start], nums[end])


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums)-1
        while start < end - 1:
            middle = (start+end)/2
            if nums[middle] > nums[end]:
                start = middle
            elif nums[middle] < nums[end]:
                end = middle
        return min(nums[start], nums[end])


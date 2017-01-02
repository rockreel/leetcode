class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or nums[0] > target:
            return 0
            
        if nums[-1] < target:
            return len(nums)
            
        start, end = 0, len(nums) - 1
        while start <= end:
            middle = (start + end) / 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                start = middle + 1
            else:
                end = middle - 1
        return start

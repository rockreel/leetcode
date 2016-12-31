class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
            
        i, j = 0, 1
        while j < len(nums):
            if nums[i] != nums[j]:
                nums[i+1], nums[j] = nums[j], nums[i+1]
                i += 1
            j += 1
        return i + 1


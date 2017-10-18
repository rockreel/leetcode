class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """          
        bp, fp = 0, 0
        while fp < len(nums):
            if nums[fp] != val:
                nums[bp], nums[fp] = nums[fp], nums[bp]
                bp += 1
            fp += 1
        return bp

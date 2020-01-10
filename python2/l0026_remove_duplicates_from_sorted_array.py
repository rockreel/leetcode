class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
            
        bp, fp = 0, 1
        while fp < len(nums):
            if nums[bp] != nums[fp]:
                nums[bp+1], nums[fp] = nums[fp], nums[bp+1]
                bp += 1
            fp += 1
        return bp + 1


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 1, len(nums) - 1
        while start < end:
            middle = (start + end) / 2
            # Num between start and middle should be less than
            # (end-start)/2+1 if no duplicate between start and middle. 
            count = len([n for n in nums if start <= n <= middle])
            if count > (end - start) / 2 + 1:
                end = middle
            else:
                start = middle + 1
        return start


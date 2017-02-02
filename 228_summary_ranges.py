class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        i = 0
        ranges = []
        while i < len(nums):
            j = i
            while j + 1 < len(nums) and nums[j+1] == nums[j]+1:
                j += 1
            if i == j:
                ranges.append(str(nums[j]))
            else:
                ranges.append('%s->%s' % (nums[i], nums[j]))
            i = j + 1
        return ranges


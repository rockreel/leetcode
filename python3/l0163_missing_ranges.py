class Solution:
    """
    @param: nums: a sorted integer array
    @param: lower: An integer
    @param: upper: An integer
    @return: a list of its missing ranges
    """
    def findMissingRanges(self, nums, lower, upper):
        # write your code here
        ranges = []
        nums = [lower-1] + nums + [upper+1]
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1] or nums[i] == nums[i+1] - 1:
                continue
            elif nums[i] == nums[i+1] - 2:
                ranges.append('%s' % (nums[i] + 1,))
            else:
                ranges.append('%s->%s' % (nums[i] + 1, nums[i+1] - 1))
        return ranges
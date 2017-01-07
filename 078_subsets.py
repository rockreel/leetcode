class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        result = []
        for subset in self.subsets(nums[1:]):
            result.append([nums[0]] + subset)
            result.append(subset)
        return result


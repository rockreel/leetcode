class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [[nums[0]]]
        result = []
        for i, n in enumerate(nums):
            for r in self.permute(nums[:i] + nums[i+1:]):
                result.append([n]+r)
        return result


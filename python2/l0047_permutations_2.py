class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [[nums[0]]]
        
        nums = sorted(nums)
        result = []
        i = 0
        while i < len(nums):
            n = nums[i]
            for r in self.permuteUnique(nums[:i] + nums[i+1:]):
                result.append([n] + r)
            while i < len(nums) and nums[i] == n:
                i += 1
        return result


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []  
        for i, n in enumerate(nums):
            for s in self.subsets(nums[i+1:]):
                result.append([n]+s)
        result.append([])
        return result


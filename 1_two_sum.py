class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complement_to_idx = {}
        for i, n in enumerate(nums):
            if n not in complement_to_idx:
                complement_to_idx[target-n] = i
            else:
                return [complement_to_idx[n], i]

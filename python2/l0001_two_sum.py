class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_idx = {}
        for i, n in enumerate(nums):
            if target - n in num_to_idx:
                return [num_to_idx[target - n], i]
            else:
                num_to_idx[n] = i

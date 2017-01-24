class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maj_idx = 0
        count = 1
        for i, n in enumerate(nums[1:], 1):
            if n == nums[maj_idx]:
                count += 1
            else:
                count -= 1
            if count == 0:
                maj_idx = i
                count = 1
        return nums[maj_idx]


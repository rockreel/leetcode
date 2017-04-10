class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maj_idx = 0
        maj_count = 0
        for i, n in enumerate(nums):
            if n == nums[maj_idx]:
                maj_count += 1
            else:
                maj_count -= 1
            if maj_count == 0:
                maj_idx = i
                maj_count = 1
        return nums[maj_idx]


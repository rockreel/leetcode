class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_jump = 0
        for i, n in enumerate(nums):
            max_jump = max(n, max_jump - 1)
            if max_jump == 0 and i < len(nums) - 1:
                return False
        return True


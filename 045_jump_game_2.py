class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = 0
        jumps = 0
        while pos < len(nums) - 1:
            # Current jump can reach the end.
            if pos + nums[pos] >= len(nums) - 1:
                jumps += 1
                break
            
            # Find the farthest position it can go with this and next jump,
            # then jump to the position can have greatest reach for the two
            # jumps combined.
            max_reach = 0
            step_to_jump = 1
            for step in range(1, min(nums[pos]+1, len(nums)-pos)):
                if nums[pos + step] + step >= max_reach:
                    max_reach = nums[pos + step] + step
                    step_to_jump = step
            pos = pos + step_to_jump
            jumps += 1
            
        return jumps


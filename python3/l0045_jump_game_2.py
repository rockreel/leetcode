from typing import List

class Solution:
    def jumpDP(self, nums: List[int]) -> int:
        # min_jumps[i] num of min jump to i.
        min_jumps = [float('inf')] * len(nums)
        min_jumps[0] = 0
        for i, n in enumerate(nums):
            for j in range(i+1, min(len(nums), i+n+1)):
                min_jumps[j] = min(min_jumps[i] + 1, min_jumps[j])
        
        return min_jumps[-1]

    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        level = 1
        step = 0
        while step + nums[step] < len(nums) - 1:
            level += 1
            max_reach = 0
            for i in range(1, nums[step]+1):
                # Check farthest reach after move i step to step+i.
                if nums[step+i] + step + i > max_reach:
                    max_reach = nums[step+i] + step + i
                    next_step = step + i
            step = next_step

        return level
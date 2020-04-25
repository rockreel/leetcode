from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i, j = 0, 0
        ranges = []
        while j < len(nums):
            while j + 1 < len(nums) and nums[j+1] == nums[j] + 1:
                j += 1
            if i == j:
                ranges.append('%s' % nums[i])
            else:
                ranges.append('%s->%s' % (nums[i], nums[j]))
            i = j + 1
            j = j + 1
        return ranges
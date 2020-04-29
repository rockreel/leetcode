from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Apply cycular linked list algorithm to identify the entry point of a loop.
        n1, n2 = 0, 0
        while True:
            n1 = nums[n1]
            n2 = nums[nums[n2]]
            if n1 == n2:
                break
        n1 = 0
        while n1 != n2:
            n1 = nums[n1]
            n2 = nums[n2]
        
        return n1
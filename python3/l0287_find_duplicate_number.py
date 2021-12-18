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

    def findDuplicateBinarySearch(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        start, end = 0, len(nums_sorted) - 1
        while start + 1 < end:
            middle = start + (end - start) // 2
            if nums_sorted[middle] >= middle + 1:
                start = middle
            else:
                end = middle
        return nums_sorted[start]
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findStart(nums: List[int], target: int) -> int:
            start, end = 0, len(nums) - 1
            while start < end:
                middle = (start + end) // 2
                if nums[middle] < target:
                    start = middle + 1
                else:
                    end = middle
            return start if nums[start] == target else -1

        def findEnd(nums: List[int], target: int) -> int:
            start, end = 0, len(nums) - 1
            while start < end:
                middle = (start + end) // 2 + 1
                if nums[middle] > target:
                    end = middle - 1
                else:
                    start = middle
            return end if nums[end] == target else -1

        if not nums:
            return [-1, -1]
        return [findStart(nums, target), findEnd(nums, target)]
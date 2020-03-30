from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            middle = (start + end) // 2
            if nums[middle] == target:
                return middle
            if nums[start] < nums[end]:
                # Regular binary search.
                if nums[middle] < target:
                    start = middle + 1
                else:
                    end = middle - 1
            else:
                # Rotated binary search
                if nums[middle] <= nums[end]:
                    # Middle is in second half.
                    if nums[middle] < target and target < nums[start]:
                        start = middle + 1
                    else:
                        end = middle - 1
                else:
                    # Middle is in first half.
                    if nums[middle] > target and target > nums[end]:
                        end = middle - 1
                    else:
                        start = middle + 1
        return -1
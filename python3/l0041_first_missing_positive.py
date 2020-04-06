from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            # Move all positive n to location n-1.
            while nums[i] <= 0 and nums[i] == i+1:
                i += 1
            while nums[i] > 0 and nums[i] - 1 < len(nums) and nums[i] != i+1:
                if nums[nums[i]-1] == nums[i]:
                    # Prevent infinite loop with duplicate numbers.
                    nums[i] = -1
                    break
                temp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = temp
            i += 1
        # Find the first location n-1, where n-1 != n, then n is the missing number.
        j = 0
        while j < len(nums) and nums[j] == j+1:
            j += 1
        return j + 1
        
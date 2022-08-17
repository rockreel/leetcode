from typing import List

class Solution:

    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # Set all number irrelevant to n+1
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        # Each num, set corresponding index to negative.
        for i in range(len(nums)):
            if abs(nums[i]) != n + 1:
                nums[abs(nums[i])-1] = -abs(nums[abs(nums[i])-1])

        # Find the first non-negative index which is the missing number.    
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1

        # If every num is negative, n + 1 is the missing number.    
        return n+1
        
    def firstMissingPositiveWhile(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            # Move all positive n to location n-1.
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
        
from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            j = i
            n = nums[j]
            while n != j + 1:
                # n should be at n - 1 position ~ k
                k = n - 1
                # Move n to k position, and take k's number for next round.
                temp = nums[k] 
                nums[k] = n
                n = temp
                j = k
            i += 1
        missing_nums = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                missing_nums.append(i+1)
        return missing_nums
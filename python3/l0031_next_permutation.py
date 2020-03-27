from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Find the position from where array need to be reversed to the end.
        reverse_from = len(nums) - 1
        while reverse_from > 0 and nums[reverse_from-1] >= nums[reverse_from]:
            reverse_from -= 1

        # If this position is not from the beginning, find the min number but
        # still greater than the number before reverse_from, and swap.
        if reverse_from > 0:
            idx_swap = reverse_from
            for i in range(reverse_from, len(nums)):
                if nums[i] <= nums[reverse_from-1]:
                    break
                idx_swap = i
            nums[reverse_from-1], nums[idx_swap] = nums[idx_swap], nums[reverse_from-1]

        # Reverse array from reverse_from to the end.
        i, j = reverse_from, len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        
        return
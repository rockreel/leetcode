from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sorted_nums = sorted(nums, reverse=True)
        nums[::2] = sorted_nums[len(nums)//2:]
        nums[1::2] = sorted_nums[:len(nums)//2]


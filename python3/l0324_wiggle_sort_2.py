class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort(reverse=True)
        n = len(nums)
        left = nums[:n//2]  # Bigger than median.
        right = nums[n//2:] # Smaller than median.
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = right[i//2]
            else:
                nums[i] = left[i//2]

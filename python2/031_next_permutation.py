class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        reverse_from = 0
        for i in range(len(nums)-1, 0, -1):
            # Search backward, find the first decrease of number.
            if nums[i] > nums[i-1]:
                # Find the next bigger one of i-i from i to end to swap with i-1.
                j = i
                while j + 1 < len(nums) and nums[j+1] > nums[i-1]:
                    j += 1
                nums[i-1], nums[j] = nums[j], nums[i-1]
                reverse_from = i
                break
                
        # Reverse part or whole list.
        j, k = reverse_from, len(nums) - 1
        while j < k:
            nums[j], nums[k] = nums[k], nums[j]
            j += 1
            k -= 1
            
        return


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        
        # Rearrange array put n at n - 1 position.
        for i in range(len(nums)):
            if nums[i] <= 0:
                continue
            # Keep swaping nums[i] with number at nums[i] - 1 position until
            # it hit a negative number or zero.
            n = nums[i]
            while True:
                if n - 1 > len(nums) - 1:
                    # If swap with out of range number, simply mark this one instead.
                    nums[i] = -1
                    break
                elif nums[n-1] == n or nums[n-1] <= 0:
                    nums[n-1] = n
                    break
                else:
                    temp = nums[n-1]
                    nums[n-1] = n
                    n = temp
        
        # Find first number mismatch with its position. 
        for i, n in enumerate(nums):
            if n != i + 1:
                return i + 1
                
        return len(nums) + 1



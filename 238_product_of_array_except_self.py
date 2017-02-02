class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Product of nums[:i].
        left_product = [1] * len(nums)
        # Product of nums[i+1:].
        right_product = [1] * len(nums)
        
        for i in range(1, len(nums)):
            left_product[i] = left_product[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            right_product[i] = right_product[i+1] * nums[i+1]
            
        return [l * r for l, r in zip(left_product, right_product)]


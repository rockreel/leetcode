class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Max/min product end at 0.
        prev_max_product = nums[0]
        prev_min_product = nums[0]
        max_product = nums[0]
        for n in nums[1:]:
            curr_max_product = max(prev_max_product*n, prev_min_product*n, n)
            curr_min_product = min(prev_max_product*n, prev_min_product*n, n)
            max_product = max(max_product, curr_max_product)
            prev_max_product = curr_max_product
            prev_min_product = curr_min_product
            
        return max_product


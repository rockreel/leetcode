from typing import List

class Solution:
    def maxProductBothDirection(self, nums: List[int]) -> int:
        max_product = float('-inf')
        product = 1
        for n in nums:
            product *= n
            max_product = max(max_product, product)
            if product == 0:
                product = 1
        product = 1
        for n in nums[::-1]:
            product *= n
            max_product = max(max_product, product)
            if product == 0:
                product = 1
        return max_product

    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        min_product = nums[0]
        result = max_product
        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_product, min_product = min_product, max_product
            max_product = max(nums[i], max_product * nums[i])
            min_product = min(nums[i], min_product * nums[i])
            result = max(max_product, result)
        
        return result
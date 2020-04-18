from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
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
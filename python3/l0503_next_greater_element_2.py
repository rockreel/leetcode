from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        result = [-1] * len(nums)
        for i, n in enumerate(nums):
            while stack and stack[-1][0] < n:
                _, index = stack.pop()
                result[index] = n
            stack.append((n, i))
        for n in nums:
            while stack and stack[-1][0] < n:
                _, index = stack.pop()
                result[index] = n
        return result

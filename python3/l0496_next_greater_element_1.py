from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_map = {}
        stack = []
        for n in nums2:
            while stack and stack[-1] < n:
                num = stack.pop()
                num_map[num] = n
            stack.append(n)
        return [num_map.get(n, -1) for n in nums1]

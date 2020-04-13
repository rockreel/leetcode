from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [(-1, -1)]  # Stack of (index, height).
        max_area = 0
        for i, h in enumerate(heights):
            while stack[-1][1] >= h:
                _, hj = stack.pop()
                max_area = max(max_area, (i - stack[-1][0] - 1) * hj)
            stack.append((i, h))

        while len(stack) > 1:
            _, hj = stack.pop()
            max_area = max(max_area, (len(heights) - stack[-1][0] - 1) * hj)
        
        return max_area
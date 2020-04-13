from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [(-1, -1)]  # Stack of (index, height).
        max_area = 0
        for i, h in enumerate(heights):
            while stack[-1][1] > h:
                j, _ = stack.pop()
                max_area = max(max_area, (j - stack[-1][0] + 1) * stack[-1][1])
            stack.append((i, h))

        while len(stack) > 1:
            j, _ = stack.pop()
            max_area = max(max_area, (j - stack[-1][0] + 1) * stack[-1][1])
        
        return max_area
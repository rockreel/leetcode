from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i, h in enumerate(heights):
            last_stack_idx = i
            while stack and stack[-1][1] > h:
                # Make sure heights in stack is increasing.
                ii, hh = stack.pop()
                last_stack_idx = ii
                # Calculate max area for every height popped out.
                max_area = max(max_area, hh * (i - ii))
            # Set inedex for each height in stack to the last index it can extend to the left.
            stack.append((last_stack_idx, h))
        # Calculate max area for heights left in stack.
        while stack:
            i, h = stack.pop()
            max_area = max(max_area, (len(heights) - i) * h)
        return max_area
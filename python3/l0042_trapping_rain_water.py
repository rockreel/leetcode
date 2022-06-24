from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left_height = [0] * len(height)  # The max height to each position's left.
        right_height = [0] * len(height)  # The max height to each position's right.
        for i in range(1, len(height)):
            left_height[i] = max(left_height[i-1], height[i-1])
        for i in range(len(height)-2, -1, -1):
            right_height[i] = max(right_height[i+1], height[i+1])
        area = 0
        for i in range(len(height)):
            area += max(min(left_height[i], right_height[i]) - height[i], 0)
        return area

    def trapMonoStack(self, height: List[int]) -> int:
        stack = []
        result = 0
        for i, h in enumerate(height):
            while stack and stack[-1][0] < h:
                h0, i0 = stack.pop()
                if stack:
                    result += (i - stack[-1][1] - 1) * (min(stack[-1][0], h) - h0)
            stack.append((h, i))
        return result
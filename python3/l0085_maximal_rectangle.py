from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        def max_rectangle_on_row(heights: List[int]) -> int:
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

        if not matrix or not matrix[0]:
            return 0

        heights = [0 for _ in range(len(matrix[0]))]
        max_area = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    heights[j] = 0
                else:
                    heights[j] += 1
            max_area = max(max_area, max_rectangle_on_row(heights))
        return max_area
        
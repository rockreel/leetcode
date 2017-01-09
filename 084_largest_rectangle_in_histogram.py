# O(n) solution.
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        
        stack = [(-1, -1)]  # Height and index.
        max_area = 0
        
        for i, h in enumerate(heights):
            while stack[-1][0] >= h:  # First item will never be poped.
                height, _ = stack.pop()
                max_area = max(max_area, height*(i - stack[-1][1] - 1))
            stack.append((h, i))
            
        while len(stack) > 1:
            height, _ = stack.pop()
            # Rest item can extend to the end of histogram.
            max_area = max(max_area, height*(len(heights) -1 - stack[-1][1]))
        
        return max_area

# O(n^2) solution, divide and conquer.
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        
        if len(heights) == 1:
            return heights[0]
        
        min_hist = min(heights)
        min_idx = heights.index(min_hist)
        
        left_square = self.largestRectangleArea(heights[:min_idx])
        right_square = self.largestRectangleArea(heights[min_idx+1:])
        
        return max(min_hist*len(heights), left_square, right_square)


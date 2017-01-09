class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        def maxRectangleInRow(heights):
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
        
        if not matrix or not matrix[0]:
            return 0
        
        # Treat each row a histogram.
        heights = [0 for _ in matrix[0]]
        max_area = 0
        for row in matrix:
            for i, cell in enumerate(row):
                if cell == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0
            max_area = max(max_area, maxRectangleInRow(heights))
            
        return max_area


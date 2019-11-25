class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        highest_to_left = [0] * len(height)
        for i in range(1, len(height)):
            highest_to_left[i] = max(highest_to_left[i-1], height[i-1])
        
        highest_to_right = [0] * len(height)
        for i in range(len(height)-2, -1, -1):
            highest_to_right[i] = max(highest_to_right[i+1], height[i+1])
            
        result = 0
        for i in range(len(height)):
            result += max(min(highest_to_left[i], highest_to_right[i]) - height[i], 0)
            
        return result


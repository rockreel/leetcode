class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    def minArea(self, image, x, y):
        # write your code here
        visited = set([(x, y)])
        stack = [(x, y)]
        x_max, x_min, y_max, y_min = x, x, y, y
        while stack:
            px, py = stack.pop()
            x_max = max(x_max, px)
            x_min = min(x_min, px)
            y_max = max(y_max, py)
            y_min = min(y_min, py)
            if px - 1 >= 0 and image[px-1][py] == '1' and (px-1, py) not in visited:
                stack.append((px-1, py))
                visited.add((px-1, py))
            if px + 1 < len(image) and image[px+1][py] == '1' and (px+1, py) not in visited:
                stack.append((px+1, py))
                visited.add((px+1, py))
            if py - 1 >= 0 and image[px][py-1] == '1' and (px, py-1) not in visited:
                stack.append((px, py-1))
                visited.add((px, py-1))
            if py + 1 < len(image[0]) and image[px][py+1] == '1' and (px, py+1) not in visited:
                stack.append((px, py+1))
                visited.add((px, py+1))    
        return (x_max - x_min + 1) * (y_max - y_min + 1)

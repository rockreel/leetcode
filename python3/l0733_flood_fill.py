from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def fill(image, sr, sc, old_color, new_color, visited):
            image[sr][sc] = new_color
            visited.add((sr, sc))
            if sr - 1 >= 0 and image[sr-1][sc] == old_color and (sr-1, sc) not in visited:
                fill(image, sr-1, sc, old_color, new_color, visited)
            if sr + 1 < len(image) and image[sr+1][sc] == old_color and (sr+1, sc) not in visited:
                fill(image, sr+1, sc, old_color, new_color, visited)
            if sc - 1 >= 0 and image[sr][sc-1] == old_color and (sr, sc-1) not in visited:
                fill(image, sr, sc-1, old_color, new_color, visited)
            if sc + 1 < len(image[0]) and image[sr][sc+1] == old_color and (sr, sc+1) not in visited:
                fill(image, sr, sc+1, old_color, new_color, visited)
                
        fill(image, sr, sc, image[sr][sc], newColor, set([]))
        return image
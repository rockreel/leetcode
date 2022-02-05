from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = deque([(0, 0, 0)])
        visited = set([])
        while queue:
            i, j, d = queue.popleft()
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 1 or (i, j) in visited:
                continue
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return d + 1
            visited.add((i, j))
            queue.append((i-1, j, d+1))
            queue.append((i+1, j, d+1))
            queue.append((i, j-1, d+1))
            queue.append((i, j+1, d+1))
            queue.append((i-1, j-1, d+1))
            queue.append((i-1, j+1, d+1))
            queue.append((i+1, j-1, d+1))
            queue.append((i+1, j+1, d+1))
        
        return -1
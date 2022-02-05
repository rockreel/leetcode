from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        fresh_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1
        if fresh_count == 0:
            return 0
        d = -1
        while queue:
            new_queue = []
            while queue:
                i, j = queue.pop(0)
                if grid[i][j] == 1:
                    grid[i][j] = 2
                    fresh_count -= 1
                if i > 0 :
                    new_queue.append((i-1, j))
                if i <= len(grid) - 2:
                    new_queue.append((i+1, j))
                if j > 0:
                    new_queue.append((i, j-1))
                if j <= len(grid[0]) - 2:
                    new_queue.append((i, j+1))
            d += 1
            queue = [n for n in new_queue if grid[n[0]][n[1]] == 1]
            # print(grid, d, new_queue)
        return d if fresh_count == 0 else -1

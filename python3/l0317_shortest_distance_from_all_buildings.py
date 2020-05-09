class Solution:
    """
    @param grid: the 2D grid
    @return: the shortest distance
    """
    def shortestDistance(self, grid):
        # write your code here
        def cal_distance(grid, row, col, dist_grid):
            # Calculate and mark min distance to building (row, col).
            queue = [(row, col, 0)]
            visited = set([(row, col)])
            while queue:
                i, j , dist = queue.pop(0)
                if (i, j) != (row, col):
                    dist_grid[i][j] = dist
                if i - 1 >= 0 and grid[i-1][j] == 0 and (i-1, j) not in visited:
                    queue.append((i-1, j, dist+1))
                    visited.add((i-1, j))
                if i + 1 < len(grid) and grid[i+1][j] == 0 and (i+1, j) not in visited:
                    queue.append((i+1, j, dist+1))
                    visited.add((i+1, j))
                if j - 1 >= 0 and grid[i][j-1] == 0 and (i, j-1) not in visited:
                    queue.append((i, j-1, dist+1))
                    visited.add((i, j-1))
                if j + 1 < len(grid[0]) and grid[i][j+1] == 0 and (i, j+1) not in visited:
                    queue.append((i, j+1, dist+1))
                    visited.add((i, j+1))
        
        dist_grids = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dist_grid = [[float('inf')] * len(grid[0]) for _ in grid]
                    cal_distance(grid, i, j, dist_grid)
                    dist_grids.append(dist_grid)
        min_dist = float('inf')
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                dist_to_all = 0
                for k in range(len(dist_grids)):
                    dist_to_all += dist_grids[k][i][j]
                min_dist = min(min_dist, dist_to_all)
        return min_dist
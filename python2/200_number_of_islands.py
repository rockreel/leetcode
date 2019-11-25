class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def fill_island(grid, i, j):
            queue = [(i, j)]
            while queue:
                row, col = queue.pop()
                grid[row][col] = 'X'
                if row - 1 >= 0 and grid[row-1][col] == '1':
                    queue.append((row-1, col))
                if row + 1 < len(grid) and grid[row+1][col] == '1':
                    queue.append((row+1, col))
                if col - 1 >= 0 and grid[row][col-1] == '1':
                    queue.append((row, col-1))
                if col + 1 < len(grid[0]) and grid[row][col+1] == '1':
                    queue.append((row, col+1))
                    
        num_island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    fill_island(grid, i, j)
                    num_island += 1
        return num_island


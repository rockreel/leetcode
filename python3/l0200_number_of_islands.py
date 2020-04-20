from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def fill(grid: List[List[str]], row: int, col: int) -> None:
            if grid[row][col] != '1':
                return
            grid[row][col] = '2'
            if row > 0:
                fill(grid, row-1, col)
            if row < len(grid) - 1:
                fill(grid, row+1, col)
            if col > 0:
                fill(grid, row, col-1)
            if col < len(grid[0]) - 1:
                fill(grid, row, col+1)
                
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    fill(grid, i, j)
                    count += 1
        return count

from typing import List

class Solution:
    def shortestPathDP(self, grid: List[List[int]], k: int) -> int:
        # Not working yet.
        m, n = len(grid), len(grid[0])
        # dp[i][j]: (steps to lower right corner, number of elemination left)
        dp = [[(0, 0) for _ in range(n)] for _ in range(m)]
        dp[-1][-1] = (0, k) if grid[-1][-1] == 0 else (0, k-1)
        for k in range(1, m+n-1):
            for i in range(m-1, m-1-k-1, -1):
                j = m + n - k - 2 - i
                if i < 0 or i > m - 1 or j < 0 or j > n - 1:
                    continue
                if i == m - 1:
                    if dp[i][j+1][0] == -1:
                        dp[i][j] = dp[i][j+1]
                    else:
                        if grid[i][j] == 0:
                            dp[i][j] = (dp[i][j+1][0] + 1, dp[i][j+1][1])
                        else:
                            if dp[i][j+1][1] - 1 >= 0:
                                dp[i][j] = (dp[i][j+1][0] + 1, dp[i][j+1][1] - 1)
                            else:
                                dp[i][j] = (-1, dp[i][j+1][1] - 1)
                elif j == n - 1:
                    if dp[i+1][j][0] == -1:
                        dp[i][j] = dp[i+1][j]
                    else:
                        if grid[i][j] == 0:
                            dp[i][j] = (dp[i+1][j][0] + 1, dp[i+1][j][1])
                        else:
                            if dp[i+1][j][1] - 1 >= 0:
                                dp[i][j] = (dp[i+1][j][0] + 1, dp[i+1][j][1] - 1)
                            else:
                                dp[i][j] = (-1, dp[i+1][j][1] - 1)
                else:
                    if dp[i+1][j][0] == -1 and dp[i][j+1][0] == -1:
                        dp[i][j] = dp[i+1][j]
                    elif dp[i+1][j][0] == -1:
                        if grid[i][j] == 0:
                            dp[i][j] = (dp[i][j+1][0] + 1, dp[i][j+1][1])
                        else:
                            if dp[i][j+1][1] - 1 >= 0:
                                dp[i][j] = (dp[i][j+1][0] + 1, dp[i][j+1][1] - 1)
                            else:
                                dp[i][j] = (-1, dp[i][j+1][1] - 1)
                    elif dp[i][j+1][0] == -1:
                        if grid[i][j] == 0:
                            dp[i][j] = (dp[i+1][j][0] + 1, dp[i+1][j][1])
                        else:
                            if dp[i+1][j][1] - 1 >= 0:
                                dp[i][j] = (dp[i+1][j][0] + 1, dp[i+1][j][1] - 1)
                            else:
                                dp[i][j] = (-1, dp[i+1][j][1] - 1)
                    else:
                        if dp[i+1][j][0] < dp[i][j+1][0]:
                            if grid[i][j] == 0:
                                dp[i][j] = (dp[i+1][j][0] + 1, dp[i+1][j][1])
                            else:
                                if dp[i+1][j][1] - 1 >= 0:
                                    dp[i][j] = (dp[i+1][j][0] + 1, dp[i+1][j][1] - 1)
                                else:
                                    dp[i][j] = (-1, dp[i+1][j][1] - 1)
                        elif dp[i+1][j][0] > dp[i][j+1][0]:
                            if grid[i][j] == 0:
                                dp[i][j] = (dp[i][j+1][0] + 1, dp[i][j+1][1])
                            else:
                                if dp[i][j+1][1] - 1 >= 0:
                                    dp[i][j] = (dp[i][j+1][0] + 1, dp[i][j+1][1] - 1)
                                else:
                                    dp[i][j] = (-1, dp[i][j+1][1] - 1)
                        else:
                            k0 = max(dp[i+1][j][1], dp[i][j+1][1])
                            if grid[i][j] == 0:
                                dp[i][j] = (dp[i][j+1][0] + 1, k0)
                            else:
                                if k0 - 1 >= 0:
                                    dp[i][j] = (dp[i][j+1][0] + 1, k0-1)
                                else:
                                    dp[i][j] = (-1, k0 - 1)

        return dp[0][0][0] # if dp[0][0][1] >= 0 else -1

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        queue = [(0, 0, k, 0, set([(0, 0)]))]
        while queue:
            i, j, k0, step, visited = queue.pop(0)
            #print(i, j, k0, step)
            if k0 < 0:
                continue
            if i == m - 1 and j == n - 1:
                return step
            if i - 1 >= 0 and (i-1, j) not in visited:
                new_visited = set(visited)
                new_visited.add((i-1, j))
                if grid[i-1][j] == 1:
                    new_k = k0 - 1
                else:
                    new_k = k0
                queue.append((i-1, j, new_k, step+1, new_visited))
            if i + 1 < m and (i+1, j) not in visited:
                new_visited = set(visited)
                new_visited.add((i+1, j))
                if grid[i+1][j] == 1:
                    new_k = k0 - 1
                else:
                    new_k = k0
                queue.append((i+1, j, new_k, step+1, new_visited))
            if j - 1 >= 0 and (i, j-1) not in visited:
                new_visited = set(visited)
                new_visited.add((i, j-1))
                if grid[i][j-1] == 1:
                    new_k = k0 - 1
                else:
                    new_k = k0
                queue.append((i, j-1, new_k, step+1, new_visited))
            if j + 1 < n and (i, j+1) not in visited:
                new_visited = set(visited)
                new_visited.add((i, j+1))
                if grid[i][j+1] == 1:
                    new_k = k0 - 1
                else:
                    new_k = k0
                queue.append((i, j+1, new_k, step+1, new_visited))
            
        return -1
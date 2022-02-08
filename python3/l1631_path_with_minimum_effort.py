from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # Dijkstra algorithm
        queue = [(0, 0)]
        shortest_paths = [[float('inf')] * len(heights[0]) for _ in heights]
        shortest_paths[0][0] = 0

        while queue:
            i, j = queue.pop(0)
            if i > 0:
                effort = max(shortest_paths[i][j], abs(heights[i][j] - heights[i-1][j]))
                if shortest_paths[i-1][j] > effort:
                    shortest_paths[i-1][j] = effort
                    queue.append((i-1, j))
            if i < len(heights) - 1:
                effort = max(shortest_paths[i][j], abs(heights[i][j] - heights[i+1][j]))
                if shortest_paths[i+1][j] > effort:
                    shortest_paths[i+1][j] = effort
                    queue.append((i+1, j))
            if j > 0:
                effort = max(shortest_paths[i][j], abs(heights[i][j] - heights[i][j-1]))
                if shortest_paths[i][j-1] > effort:
                    shortest_paths[i][j-1] = effort
                    queue.append((i, j-1))
            if j < len(heights[0]) - 1:
                effort = max(shortest_paths[i][j], abs(heights[i][j] - heights[i][j+1]))
                if shortest_paths[i][j+1] > effort:
                    shortest_paths[i][j+1] = effort
                    queue.append((i, j+1))

        return shortest_paths[-1][-1]
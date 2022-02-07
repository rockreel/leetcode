from typing import List
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        shortest_paths = [float('inf')] * n
        shortest_paths[k-1] = 0
        queue = [k]
        graph = defaultdict(list)
        for t in times:
            graph[t[0]].append((t[1], t[2]))
        while queue:
            node = queue.pop(0)
            for neighbor, travel_time in graph[node]:
                # No visited set but decide if enqueue again based on existing shortest path and current path.
                if shortest_paths[neighbor-1] > shortest_paths[node-1] + travel_time:
                    shortest_paths[neighbor-1] = shortest_paths[node-1] + travel_time
                    queue.append(neighbor)

        min_time = max(shortest_paths)
        return min_time if min_time != float('inf') else -1
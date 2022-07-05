from typing import List
from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for t in times:
            # Align node id to index.
            graph[t[0]-1].append((t[1]-1, t[2]))
            
        shortest_dist = [float('inf')] * n
        shortest_dist[k-1] = 0
        visited = set([])
        while True:
            min_time = float('inf')
            node_to_visit = None
            # Iterate through all nodes.
            for i in range(n):
                if shortest_dist[i] < min_time and i not in visited:
                    node_to_visit = i
                    min_time = shortest_dist[i]
            if node_to_visit is None:
                break
            visited.add(node_to_visit)
            # Update neighbors' shortest distance.
            for neighbor, time in graph[node_to_visit]:
                if time + shortest_dist[node_to_visit] < shortest_dist[neighbor]:
                    shortest_dist[neighbor] = time + shortest_dist[node_to_visit]

        return max(shortest_dist) if  len(visited) == n else -1

    def networkDelayTimeHeapOptimized(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for t in times:
            # Align node id to index.
            graph[t[0]-1].append((t[1]-1, t[2]))
            
        shortest_dist = [float('inf')] * n
        shortest_dist[k-1] = 0
        visited = set([])
        heap = [(0, k-1)]
        while heap:
            min_time, node_to_visit = heapq.heappop(heap)
            if node_to_visit in visited:
                continue
            else:
                visited.add(node_to_visit)
            
            for neighbor, time in graph[node_to_visit]:
                if time + shortest_dist[node_to_visit] < shortest_dist[neighbor]:
                    shortest_dist[neighbor] = time + shortest_dist[node_to_visit]
                    heapq.heappush(heap, (shortest_dist[neighbor], neighbor))

        return max(shortest_dist) if  len(visited) == n else -1

    def networkDelayTimeOptimized(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra algorithm.
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
from typing import List
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        shortest_paths = [float('inf')] * n
        shortest_paths[src] = 0
        # For each node, the list of nodes come into this node and weight.
        graph_in = defaultdict(list)
        for f in flights:
            graph_in[f[1]].append((f[0], f[2]))
        j = 0
        while j < k + 1:
            new_shortest_paths = [float('inf')] * n
            new_shortest_paths[src] = 0
            for i in range(n):
                if i == src:
                    continue
                shortest_path = float('inf')
                for from_node, weight in graph_in[i]:
                    shortest_path = min(shortest_path, shortest_paths[from_node] + weight)
                new_shortest_paths[i] = shortest_path
            shortest_paths = new_shortest_paths
            j += 1

        return shortest_paths[dst] if shortest_paths[dst] != float('inf') else -1
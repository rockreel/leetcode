from typing import List
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs(s, d, graph, visited):
            if s not in graph or d not in graph:
                return -1.0
            if s == d:
                return 1.0
            visited.add(s)
            for node in graph[s]:
                if node[0] not in visited:
                    res = dfs(node[0], d, graph, visited)
                    if res != -1.0:
                        return res * node[1]
            return -1.0
        
        graph = defaultdict(list)
        for e, v in zip(equations, values):
            graph[e[0]].append((e[1], v))
            graph[e[1]].append((e[0], 1 / v))
        return [dfs(q[0], q[1], graph, set([])) for q in queries]
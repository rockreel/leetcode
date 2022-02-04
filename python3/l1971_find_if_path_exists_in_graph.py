from typing import List
from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        queue = [source]
        visited = set([])
        while queue:
            n = queue.pop(0)
            if n == destination:
                return True
            visited.add(n)
            for c in graph[n]:
                if c not in visited:
                    queue.append(c)
                    
        return False
    
    def validPathDFS(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def hasValidPath(s, d, graph, visited):
            if s == d:
                return True
            visited.add(s)
            for n in graph[s]:
                if n not in visited:
                    res = hasValidPath(n, d, graph, visited)
                    if res:
                        return True
            visited.remove(s)
            return False
        
        graph = defaultdict(list)
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
                    
        return hasValidPath(source, destination, graph, set([]))
        
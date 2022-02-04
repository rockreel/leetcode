from typing import List

class Solution:

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        def allPaths(s, d, graph, visited):
            if s == d:
                return [[d]]
            result = []
            visited.add(s)
            for n in graph[s]:
                if n not in visited:
                    for p in allPaths(n, d, graph, visited):
                        result.append([s] + p)
            visited.remove(s)
            return result
        
        return allPaths(0, len(graph) - 1, graph, set([]))
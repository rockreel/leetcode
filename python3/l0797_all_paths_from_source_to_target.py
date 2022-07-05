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
    
    def allPathsSourceTargetIterative(self, graph: List[List[int]]) -> List[List[int]]: 
        stack = [(0, [0])]
        paths = []
        while stack:
            v, path = stack.pop()
            if v == len(graph) - 1:
                paths.append(path)
                continue
            for n in graph[v]:
                stack.append((n, path + [n]))
        return paths
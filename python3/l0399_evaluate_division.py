from typing import List
from collections import defaultdict

class Solution:

    def __init__(self):
        # e = v * root, store (root, v) in self._root
        self._root = {}
        
    # Find with path compression.
    def find(self, e):
        if e not in self._root:
            return None
        curr = self._root[e]
        if curr[0] == e:
            return curr
        root = self.find(curr[0])
        self._root[e] = (root[0], curr[1] * root[1])
        return self._root[e]
    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        for e, v in zip(equations, values):
            self._root[e[0]] = (e[0], 1.0)
            self._root[e[1]] = (e[1], 1.0)
            
        # Union.
        for e, v in zip(equations, values):
            root0 = self.find(e[0])
            root1 = self.find(e[1])
            if root0[0] != root1[0]:
                self._root[root0[0]] = (root1[0], v * root1[1] / root0[1] )
        
        # Query.
        result = []
        for q in queries:
            root0 = self.find(q[0])
            root1 = self.find(q[1])
            if root0 is None or root1 is None:
                result.append(-1.0)
            elif root0[0] != root1[0]:
                result.append(-1.0)
            else:
                result.append(root0[1] / root1[1])
                
        return result

    def calcEquationDFS(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
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
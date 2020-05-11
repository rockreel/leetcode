from collections import defaultdict
from typing import List

class Solution(object):
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        vertices = set(range(n))
        vertex_map = defaultdict(list)
        num = 0
        for e in edges:
            vertex_map[e[0]].append(e[1])
            vertex_map[e[1]].append(e[0])

        while vertices:
            vertex = vertices.pop()
            queue = [vertex]
            # visited.add(vertex)
            while queue:
                v = queue.pop(0)
                for n in vertex_map[v]:
                    if n in vertices:
                        queue.append(n)
                        vertices.remove(n)
            num += 1

        return num

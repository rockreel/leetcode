import heapq
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = []
        edges = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                edges.append((abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1]), i, j))
        heapq.heapify(edges)
        count = 0
        distance = 0
        union_find = UnionFind(len(points))
        while count < len(points) - 1:
            d, i, j = heapq.heappop(edges)
            if not union_find.connected(i, j):
                distance += d
                union_find.union(i, j)
                count += 1
        return distance


class UnionFind:
    def __init__(self, size):
        self._root = list(range(size))
        self._rank = [1] * size
        
    def find(self, x):
        if x == self._root[x]:
            return x
        self._root[x] = self.find(self._root[x])
        return self._root[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self._rank[root_x] > self._rank[root_y]:
                self._root[root_y] = root_x
            elif self._rank[root_x] < self._rank[root_y]:
                self._root[root_x] = root_y
            else:
                self._root[root_y] = root_x
                self._rank[root_x] += 1
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)
        
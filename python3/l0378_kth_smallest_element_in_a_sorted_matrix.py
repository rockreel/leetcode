import heapq
from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = [(matrix[0][0], 0, 0)]
        visited = set([(0, 0)])
        while k > 1:
            _, i, j = heapq.heappop(heap)
            if i + 1 < len(matrix) and (i+1, j) not in visited:
                heapq.heappush(heap, (matrix[i+1][j], i+1, j))
                visited.add((i+1, j))
            if j + 1 < len(matrix[0]) and (i, j+1) not in visited:
                heapq.heappush(heap, (matrix[i][j+1], i, j+1))
                visited.add((i, j+1))
            k -= 1
        return heap[0][0]
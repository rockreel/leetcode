import heapq
from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for i in range(len(mat)):
            num_soldiers = sum(mat[i])
            if len(heap) < k:
                heapq.heappush(heap, (-num_soldiers, -i))
            else:
                if (-num_soldiers, -i) > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-num_soldiers, -i))
        return [h[1] for h in sorted([(-h[0], -h[1]) for h in heap])]
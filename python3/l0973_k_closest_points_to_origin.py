from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            d = p[0]*p[0] + p[1]*p[1]
            if len(heap) < k:
                heapq.heappush(heap, (-d, p))
            else:
                if -d > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-d, p))
        return [h[1] for h in heap]
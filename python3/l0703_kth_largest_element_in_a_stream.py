from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._k = k
        self._heap = []
        for n in nums:
            self._heap_add(n)

    def add(self, val: int) -> int:
        self._heap_add(val)
        return self._heap[0]
    
    def _heap_add(self, val: int):
        if len(self._heap) < self._k:
            heapq.heappush(self._heap, val)
        else:
            if val > self._heap[0]:
                heapq.heappop(self._heap)
                heapq.heappush(self._heap, val)
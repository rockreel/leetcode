import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._min_heap = []
        self._max_heap = []

    def addNum(self, num: int) -> None:
        if len(self._min_heap) > len(self._max_heap):
            value = heapq.heappop(self._min_heap)
            heapq.heappush(self._min_heap, max(value, num))
            heapq.heappush(self._max_heap, -min(value, num))
        elif len(self._min_heap) < len(self._max_heap):
            value = -heapq.heappop(self._max_heap)
            heapq.heappush(self._min_heap, max(value, num))
            heapq.heappush(self._max_heap, -min(value, num))
        else:
            if self._min_heap and num >= self._min_heap[0]:
                heapq.heappush(self._min_heap, num)
            else:
                heapq.heappush(self._max_heap, -num)

    def findMedian(self) -> float:
        if len(self._min_heap) > len(self._max_heap):
            return self._min_heap[0]
        elif len(self._min_heap) < len(self._max_heap):
            return -self._max_heap[0]
        else:
            return (self._min_heap[0] - self._max_heap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        import heapq
        self._min_heap = []
        self._max_heap = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if not self._min_heap or num < self._min_heap[0]:
            heapq.heappush(self._max_heap, -num)
        else:
            heapq.heappush(self._min_heap, num)
        while len(self._min_heap) > len(self._max_heap) + 1:
            heapq.heappush(self._max_heap, -heapq.heappop(self._min_heap))
        while len(self._max_heap) > len(self._min_heap):
            heapq.heappush(self._min_heap, -heapq.heappop(self._max_heap))
        

    def findMedian(self):
        """
        :rtype: float
        """
        if not self._min_heap:
            return None
        if len(self._min_heap) == len(self._max_heap):
            return float((self._min_heap[0]-self._max_heap[0])) / 2
        else:
            return float(self._min_heap[0])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


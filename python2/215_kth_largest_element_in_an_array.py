class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        heap = []
        for n in nums:
            if len(heap) < k:
                heapq.heappush(heap, n)
            else:
                if n > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, n)
        return heap[0]


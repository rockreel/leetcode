from typing import List
import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        brick_sum = 0
        for i in range(0, len(heights)-1):
            if heights[i+1] <= heights[i]:
                continue
            diff = heights[i+1] - heights[i]
            if len(heap) < ladders:
                heapq.heappush(heap, diff)
            else:
                if heap and diff > heap[0]:
                    brick_sum += heapq.heappop(heap)
                    heapq.heappush(heap, diff)
                else:
                    brick_sum += diff
            if brick_sum > bricks:
                return i
        return len(heights) - 1
from common import ListNode
import heapq
from typing import List

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        min_heap = []
        pointers = []
        for i, l in enumerate(lists):
            if l is not None:
                heapq.heappush(min_heap, (l.val, i))
            pointers.append(l)
            
        dummy = ListNode(None)
        p = dummy
        while len(min_heap) > 0:
            val, idx = heapq.heappop(min_heap)
            p.next = ListNode(val)
            p = p.next
            pointers[idx] = pointers[idx].next
            if pointers[idx]:
                heapq.heappush(min_heap, (pointers[idx].val, idx))

        return dummy.next

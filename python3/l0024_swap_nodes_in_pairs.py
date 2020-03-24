from common import ListNode

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        p = dummy
        
        while p.next and p.next.next:
            # Locate next two nodes.
            p0 = p.next
            p1 = p.next.next
            # Swap p0 and p1.
            p0.next = p1.next
            p1.next = p0
            p.next = p1
            # Proceed p.
            p = p.next.next
            
        return dummy.next
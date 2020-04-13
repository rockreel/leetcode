from common import ListNode

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = p0 = ListNode(None)
        dummy.next = head

        # Find node before the reverse section.
        i = 0
        while p0.next and i < m - 1:
            p0 = p0.next
            i += 1
        
        # Reverse m to n node.
        if not p0.next or not p0.next.next:
            return head
        p1 = p0.next
        p2 = p0.next.next
        i = 0
        while p2 and i < n - m:
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3
            i += 1
        
        # Link up reversed section with rest part.
        p0.next.next = p2
        p0.next = p1
        
        return dummy.next
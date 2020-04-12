from common import ListNode

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        p1 = h1 = ListNode(None)
        p2 = h2 = ListNode(None)
        p = head
        while p:
            if p.val < x:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            p = p.next
        p1.next = h2.next
        p2.next = None
        return h1.next
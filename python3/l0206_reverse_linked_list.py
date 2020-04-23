from common import ListNode

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        p0, p1, p2 = None, head, head.next
        while p1:
            p1.next = p0
            p0 = p1
            p1 = p2
            p2 = p2.next if p2 else None
        return p0
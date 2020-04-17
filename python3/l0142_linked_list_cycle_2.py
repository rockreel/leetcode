from common import ListNode

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        p1, p2 = head, head
        while p2 and p2.next:
            p2 = p2.next.next
            p1 = p1.next
            if p1 == p2:
                p1 = head
                while p1 != p2:
                    p2 = p2.next
                    p1 = p1.next
                return p1
        return None
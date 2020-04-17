from common import ListNode

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        p1, p2 = head, head
        while p2 and p2.next:
            p2 = p2.next.next
            p1 = p1.next
            if p1 == p2:
                return True
        return False
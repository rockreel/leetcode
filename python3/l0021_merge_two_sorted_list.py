from common import ListNode

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(None)
        p, p1, p2 = dummy, l1, l2
        while p1 or p2:
            if p1 is None:
                p.next = p2
                p2 = p2.next
            elif p2 is None:
                p.next = p1
                p1 = p1.next
            else:
                if p1.val < p2.val:
                    p.next = p1
                    p1 = p1.next
                else:
                    p.next = p2
                    p2 = p2.next
            p = p.next
        return dummy.next

from common import ListNode 

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd = ListNode(0)
        even = ListNode(0)
        p, po, pe = head, odd, even
        while p:
            po.next = p
            pe.next = p.next
            po = po.next
            pe = pe.next
            p = p.next.next if p.next else None
        po.next = even.next
        return odd.next

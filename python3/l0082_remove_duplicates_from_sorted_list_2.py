from common import ListNode

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummy = ListNode(None)
        dummy.next = head
        p0, p1 = dummy, dummy.next.next
        while p1:
            if p1.val != p0.next.val:
                p0 = p0.next
            else:
                while p1 and p1.val == p0.next.val:
                    p1 = p1.next
                p0.next = p1
            p1 = p1.next if p1 else None
        return dummy.next

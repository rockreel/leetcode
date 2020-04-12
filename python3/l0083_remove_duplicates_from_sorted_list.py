from common import ListNode

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        p0, p1 = head, head.next
        while p1:
            if p1.val != p0.val:
                p0 = p0.next
            else:
                p0.next = p1.next
            p1 = p1.next
        return head
        
from common import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        f, b = dummy, dummy
        i = 0
        while i < n:
            f = f.next
            i += 1
        while f.next:
            f = f.next
            b = b.next
        b.next = b.next.next
        return dummy.next
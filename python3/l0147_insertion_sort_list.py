from common import ListNode

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        p = dummy  # p.next is the node to insertion.
        while p.next:
            p0 = dummy  # p0.next is the position to insert.
            while p0 != p and p0.next.val < p.next.val:
                p0 = p0.next
            node = p.next
            # Detach the node.
            p.next = node.next
            # Insert the node.
            node.next = p0.next
            p0.next = node
            # Advance p if no actual insertion happen.
            if p0 == p:
                p = p.next
        return dummy.next
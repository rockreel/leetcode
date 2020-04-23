from common import ListNode

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        p = dummy = ListNode(0)
        dummy.next = head
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return dummy.next
        

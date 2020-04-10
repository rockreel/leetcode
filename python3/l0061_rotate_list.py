from common import ListNode

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0:
            return head
        
        tail, length = head, 1
        while tail.next:
            length += 1
            tail = tail.next
        
        k = k % length
        if k == 0:
            return head
        
        i = length - k - 1
        middle = head
        while i > 0:
            i -= 1
            middle = middle.next
        
        tail.next = head
        head = middle.next
        middle.next = None
        return head
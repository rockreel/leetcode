from common import ListNode

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k < 2:
            return head

        next_group, i = head, 0
        while next_group and i < k:
            next_group = next_group.next
            i += 1
        
        if i < k:
            return head
        
        p1, p2 = head, head.next
        while p2 != next_group:
            temp = p2.next
            p2.next = p1
            p1 = p2
            p2 = temp
        new_head = p1
        head.next = self.reverseKGroup(next_group, k)
        return new_head
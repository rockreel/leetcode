# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k < 2 or not head:
            return head
            
        # Determin if there are k nodes.
        p = head
        i = 0
        while p and i < k:
            p = p.next
            i += 1
        if i < k:  # Less than k nodes.
            return head
            
        # Reverse first k nodes and do it recursively.
        next_block_head = p
        p1, p2 = head, head.next
        while p2 != next_block_head:
            next = p2.next
            p2.next = p1
            p1 = p2
            p2 = next
        new_head = p1
        # Old head now is the tail, connect it to next block head.
        head.next = self.reverseKGroup(next_block_head, k)
        return new_head


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        
        # Find length of list and get the tail node.
        p1 = head
        len = 1
        while p1.next:
            p1 = p1.next
            len += 1
            
        k = k % len
        if k == 0:
            return head
        
        # Search and rotate.
        p2 = head
        i = 0
        while i < len - k - 1:
            p2 = p2.next
            i += 1
            
        p1.next = head
        head = p2.next 
        p2.next = None
        
        return head


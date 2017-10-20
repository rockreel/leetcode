# percentage: 23.62%
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        
        p1 = dummy  # Fisrt pointer.
        p2 = dummy  # Second pointer.
        i = 0
        
        while i < n:
            p1 = p1.next
            i += 1
        while p1.next:
            p1 = p1.next
            p2 = p2.next
    
        # Remove node.
        p2.next = p2.next.next
        return dummy.next

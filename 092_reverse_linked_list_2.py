# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        
        # Find the reverse starting point.
        dummy = ListNode(None)
        dummy.next = head
        first_tail = dummy  # Tail of the first not reversed part.
        i = 0
        while first_tail.next and i < m - 1:
            first_tail = first_tail.next
            i += 1
        
        # Reverse from mth to nth nodes.
        pb = first_tail.next  # Back pointer.
        pf = pb.next          # Front pointer.
        i = 0
        while i < n - m:
            tmp = pf.next
            pf.next = pb
            pb = pf
            pf = tmp
            i += 1
            
        # Relink.
        first_tail.next.next = pf
        first_tail.next = pb
        
        return dummy.next


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1, p2 = headA, headB
        while p1 and p2:
            p1 = p1.next
            p2 = p2.next
            
        if p1:  # A is longer, p1 points to longer list.
            p = p1
            p1, p2 = headA, headB
        else:  # B is longer, p1 ponts to longer list.
            p = p2
            p1, p2 = headB, headA
            
        # Move longer list pointer first, then move both
        # together until they meet.
        while p and p1:
            p1 = p1.next
            p = p.next
        while p1 and p2 and p1 != p2:
            p1 = p1.next
            p2 = p2.next
        
        return p1 if p1 == p2 else None


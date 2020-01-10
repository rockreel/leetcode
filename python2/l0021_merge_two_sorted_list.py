# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(None)
        p1, p2, l = l1, l2, head
        while p1 and p2:
            if p1.val < p2.val:
                l.next = p1
                p1 = p1.next
            else:
                l.next = p2
                p2 = p2.next
            l = l.next
        
        while p1:
            l.next = p1
            l, p1 = l.next, p1.next
        while p2:
            l.next = p2
            l, p2 = l.next, p2.next
            
        return head.next
        

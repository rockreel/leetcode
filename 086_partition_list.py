# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy1 = ListNode(None)
        dummy1.next = head
        dummy2 = ListNode(None)
        p1, p2 = dummy1, dummy2
        
        while p1.next:
            if p1.next.val < x:
                p2.next = p1.next
                p1.next = p1.next.next
                p2 = p2.next
            else:
                p1 = p1.next
            
        p2.next = dummy1.next
        return dummy2.next


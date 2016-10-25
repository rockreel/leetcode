# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1, p2 = l1, l2
        r = ListNode(None)
        p = r
        carry = 0
        while p1 or p2:
            if p1:
                p1_val = p1.val
                p1 = p1.next
            else:
                p1_val = 0
            if p2:
                p2_val = p2.val
                p2 = p2.next
            else:
                p2_val = 0
            
            result = p1_val + p2_val + carry
    
            if result > 9:
                result = result - 10
                carry = 1
            else:
                carry = 0
                
            p.next = ListNode(result)
            p = p.next
        if carry:
            p.next = ListNode(1)
            
        return r.next

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next or not head.next.next:
            return head
        # p points to last node of processed odd portion.
        # q points to last node of processed even portion.
        # odd ... odd (p) -> even ... even (q) -> odd -> even -> odd ...
        p, q = head, head.next
        while q and q.next:
            tmp1 = p.next
            tmp2 = q.next.next
            p.next = q.next
            q.next.next = tmp1
            q.next = tmp2
            p = p.next
            q = q.next
        return head


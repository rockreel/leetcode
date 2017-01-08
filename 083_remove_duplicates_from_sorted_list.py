# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pf, pb = head, head
        while pb:
            while pf.next and pf.next.val == pf.val:
                pf = pf.next
            pb.next = pf.next
            pb = pb.next
            pf = pb
        return head


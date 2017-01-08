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
        dummy = ListNode(None)
        dummy.next = head
        pb = dummy
        pf, pc = head, head
        while pc:
            while pf.next and pf.next.val == pf.val:
                pf = pf.next
            if pf == pc:
                # No duplicates.
                pf = pf.next
                pc = pc.next
                pb = pb.next
            else:
                # Duplciates
                pb.next = pf.next
                pc = pf.next
                pf = pf.next
        return dummy.next


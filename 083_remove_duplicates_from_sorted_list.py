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
        p1, p2 = dummy, head
        while p2:
            if p2.val != p1.val:
                p1 = p1.next
                p2 = p2.next
            else:
                p1.next = p2.next
                p2 = p2.next
        return dummy.next


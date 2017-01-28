# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        p = head
        next = p.next
        prev = None
        while p:
            p.next = prev
            prev = p
            p = next
            if next:
                next = next.next
        return prev


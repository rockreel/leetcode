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
            num_dup = 0
            while p2 and p2.val == p1.next.val:
                num_dup += 1
                p2 = p2.next
            if num_dup > 1:
                p1.next = p2
            else:
                p1 = p1.next
        return dummy.next

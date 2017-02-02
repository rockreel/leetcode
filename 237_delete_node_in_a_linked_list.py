# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        p1, p2 = node, None
        while p1.next:
            p1.val = p1.next.val
            p2 = p1
            p1 = p1.next
        p2.next = None


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        # Less than 3 nodes, return directly.
        if not head or not head.next or not head.next.next:
            return
        
        # Find the middle
        stack = []
        p1, p2 = head, head
        while p2 and p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next
        
        # Break list
        temp = p1.next
        p1.next = None
        p1 = temp
        
        # Push nodes from 2nd half to stack.
        while p1:
            stack.append(p1)
            p1 = p1.next
        
        # Reorder.
        p1 = head
        while stack:
            node = stack.pop()
            temp = p1.next
            p1.next = node
            p1 = temp
            node.next = p1


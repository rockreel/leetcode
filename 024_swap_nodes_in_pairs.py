# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
            
        next_list = head.next.next
        new_head = head.next
        new_head.next = head
        head.next = self.swapPairs(next_list)
        
        return new_head
        

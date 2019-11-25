# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        current = head
        while current:
            # Find insert position.
            insert_to = dummy
            while insert_to.next and insert_to.next.val < current.val:
                insert_to = insert_to.next
            # Keep next node to be inserted.
            next_current = current.next
            # Insert node.
            temp = insert_to.next
            insert_to.next = current
            current.next = temp
            # Proceed to next node.
            current = next_current
            
        return dummy.next


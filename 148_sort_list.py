# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def sort(head, length):
            if length == 0:
                return (None, None)
                
            if length == 1:
                next_head = head.next
                head.next = None
                return (head, next_head)
            
            # Sort 1st and 2nd halfs.
            head1, head2 = sort(head, length/2)
            head2, next_head = sort(head2, length/2+length%2)
            
            # Merge 2 sorted list.
            dummy = ListNode(None)
            p, p1, p2 = dummy, head1, head2
            while p1 and p2:
                if p1.val < p2.val:
                    p.next = p1
                    p1 = p1.next
                else:
                    p.next = p2
                    p2 = p2.next
                p = p.next
            while p1:
                p.next = p1
                p = p.next
                p1 = p1.next
            while p2:
                p.next = p2
                p = p.next
                p2 = p2.next
                
            return (dummy.next, next_head)
        
        # Count list length.
        p, length = head, 0
        while p:
            length += 1
            p = p.next
        head, _ = sort(head, length)
        return head


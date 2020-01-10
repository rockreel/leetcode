# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p1, p2 = head, head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                break
        else:
            # Not meet, so no circle.
            return None
            
        # When p1 meet p2 again, it is the circle start.
        p1 = head
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1


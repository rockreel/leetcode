from common import ListNode

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        p = node
        while True:
            p.val = p.next.val
            if not p.next.next:
                p.next = None
                break
            p = p.next
        
        return

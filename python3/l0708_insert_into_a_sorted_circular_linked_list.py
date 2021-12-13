class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param node: a list node in the list
    @param x: An integer
    @return: the inserted new list node
    """
    def insert(self, node, x):
        # write your code here
        n = ListNode(x)

        if not node:
            n.next = n
            return n

        if not node.next:
            n.next = node
            node.next = n
            return n

        # Find the position sorted order breaks.
        p = node
        while p.val <= p.next.val:
            p = p.next
            if p == node:
                break
        drop_point = p  # Where next node is smaller and sorted order breaks.
        
        # Find position to insert after drop point.
        while p.next.val < x:
            p = p.next
            if p == drop_point:
                break
            
        n.next = p.next
        p.next = n

        return n
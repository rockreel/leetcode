from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def flattenNode(head: Optional[Node]):
            # Flatten list and return head and tail of new list.
            if not head:
                return None, None
            tail = head  # Tail to return.
            p = head
            while p:
                next = p.next
                head0, tail0 = flattenNode(p.child)
                if head0 and tail0:
                    p.next = head0
                    head0.prev = p
                    tail0.next = next
                    if next:
                        next.prev = tail0
                    tail = tail0
                else:
                    tail = p
                p.child = None
                p = next
            return head, tail
        
        head, _ = flattenNode(head)
        return head
from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Create a interweaving list with old and new node alternating.
        p = head
        while p:
            node = Node(p.val)
            next = p.next
            p.next = node
            node.next = next
            p = next
        # Link random point in new nodes.
        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next
        # Separate new and old nodes to get copy of the list.
        dummy = Node(0)
        p, q = head, dummy
        while p:
            next = p.next.next
            q.next = p.next
            p.next = next
            p = next
            q = q.next
        return dummy.next

    def copyRandomList2(self, head: 'Node') -> 'Node':
        dummy = p0 = Node(0)
        dummy.next = head
        p1 = head
        node_map = dict()
        # Copy linked list.
        while p1:
            node = Node(p1.val)
            p0.next = node
            node_map[p1] = node
            p1 = p1.next
            p0 = p0.next
        # Link random pointers.
        p0 = dummy.next
        p1 = head
        while p1:
            if p1.random is not None:
                p0.random = node_map[p1.random]
            p0 = p0.next
            p1 = p1.next
        return dummy.next
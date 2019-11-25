# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

# Solution without using extra hash map.
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        # Insert each copied node in the original list.
        p = head
        while p:
            node = RandomListNode(p.label)
            next_node = p.next
            p.next = node
            node.next = next_node
            p = p.next.next
            
        # Link random pointer.
        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next
        
        # Decouple list.
        dummy = RandomListNode(0)
        p, q = head, dummy
        while p:
            q.next = p.next
            p.next = p.next.next
            q = q.next
            p = p.next
        
        return dummy.next

# Hash map solution.
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        node_map = {}
        dummy = RandomListNode(0)
        # Copy list.
        p, q = head, dummy
        while p:
            node = RandomListNode(p.label)
            node_map[p] = node
            q.next = node
            q = q.next
            p = p.next
        
        # Link random pointer.
        p, q = head, dummy.next
        while p:
            if p.random:
                q.random = node_map[p.random]
            p = p.next
            q = q.next
            
        return dummy.next


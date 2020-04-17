class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = [root]
        while queue:
            queue_next = []
            while queue:
                node = queue.pop(0)
                node.next = queue[0] if queue else None
                if node.left:
                    queue_next.append(node.left)
                if node.right:
                    queue_next.append(node.right)
            queue = queue_next
        return root
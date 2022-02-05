# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


from typing import List
from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        levels = []
        while queue:
            new_queue = deque([])
            levels.append([])
            while queue:
                n = queue.popleft()
                levels[-1].append(n.val)
                for c in n.children:
                    new_queue.append(c)
            queue = new_queue
        return levels
                
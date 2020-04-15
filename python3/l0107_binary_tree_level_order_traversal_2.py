from common import TreeNode
from typing import List

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        levels = []
        while queue:
            levels.append([])
            queue_next = []
            while queue:
                node = queue.pop(0)
                levels[-1].append(node.val)
                if node.left:
                    queue_next.append(node.left)
                if node.right:
                    queue_next.append(node.right)
            queue = queue_next

        return levels[::-1]
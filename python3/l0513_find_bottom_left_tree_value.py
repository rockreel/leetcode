from common import TreeNode
from typing import Optional

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = []
        result = None
        if root:
            queue.append(root)
        while queue:
            new_queue = []
            result = queue[0].val
            while queue:
                node = queue.pop(0)
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            queue = new_queue
        return result

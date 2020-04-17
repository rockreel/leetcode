from common import TreeNode
from typing import List

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root] if root else []
        nodes = []
        while stack:
            node = stack.pop()
            nodes.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return nodes
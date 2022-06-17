from common import TreeNode
from typing import List, Optional

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        current = root
        previous = None
        stack = []
        nodes = []
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                if stack[-1].right is None or stack[-1].right == previous:
                    node = stack.pop()
                    nodes.append(node.val)
                    previous = node
                else:
                    current = stack[-1].right
        return nodes
    
    def postorderTraversalUniversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []
        if root:
            stack.append(root)
        while stack:
            if stack[-1]:
                n = stack.pop()
                stack.append(n)
                stack.append(None)
                if n.right:
                    stack.append(n.right)
                if n.left:
                    stack.append(n.left)
            else:
                stack.pop()
                n = stack.pop()
                result.append(n.val)
        return result
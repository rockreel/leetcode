from common import TreeNode
from typing import List

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
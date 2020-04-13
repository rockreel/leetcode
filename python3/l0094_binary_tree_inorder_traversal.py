from common import TreeNode
from typing import List

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        nodes = []
        stack = []
        current = root
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                if stack:
                    node = stack.pop()
                    nodes.append(node.val)
                    if node.right:
                        current = node.right
        return nodes


    def inorderTraversalRecursive(self, root: TreeNode) -> List[int]:
        def inorder_traverse(root: TreeNode, nodes: List[int]):
            if not root:
                return
            inorder_traverse(root.left, nodes)
            nodes.append(root.val)
            inorder_traverse(root.right, nodes)

        nodes = []
        inorder_traverse(root, nodes)
        return nodes

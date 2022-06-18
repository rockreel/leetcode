from common import TreeNode
from typing import Optional

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def sum_left_leaf(root, is_left_child):
            if not root:
                return 0
            if not root.left and not root.right:
                if is_left_child:
                    return root.val
                else:
                    return 0
            return sum_left_leaf(root.left, True) + sum_left_leaf(root.right, False)
        return sum_left_leaf(root, False)

    def sumOfLeftLeavesIterative(self, root: Optional[TreeNode]) -> int:
        stack = []
        if root:
            stack.append((root, False))
        result = 0
        while stack:
            node, is_left_child = stack.pop()
            if is_left_child and not node.left and not node.right:
                result += node.val
            if node.right:
                stack.append((node.right, False))
            if node.left:
                stack.append((node.left, True))
        return result
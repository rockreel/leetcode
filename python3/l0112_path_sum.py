from common import TreeNode
from typing import Optional

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        
        if not root.left and not root.right:
            return root.val == sum

        if self.hasPathSum(root.left, sum - root.val):
            return True

        if self.hasPathSum(root.right, sum - root.val):
            return True

        return False

    def hasPathSumIterative(self, root: Optional[TreeNode], targetSum: int) -> bool:
        queue = []
        if root:
            queue.append((root, targetSum))
        while queue:
            node, target = queue.pop(0)
            if not node.left and not node.right and node.val == target:
                return True
            if node.left:
                queue.append((node.left, target - node.val))
            if node.right:
                queue.append((node.right, target - node.val))
        return False
        
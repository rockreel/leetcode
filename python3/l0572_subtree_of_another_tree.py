from typing import Optional
from common import TreeNode

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same_tree(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False
            return is_same_tree(root1.left, root2.left) and is_same_tree(root1.right, root2.right)
        
        if is_same_tree(root, subRoot):
            return True
        return (root.left is not None and self.isSubtree(root.left, subRoot)) or (root.right is not None and self.isSubtree(root.right, subRoot))
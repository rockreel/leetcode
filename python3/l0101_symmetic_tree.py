from common import TreeNode

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def is_mirror(root1: TreeNode, root2: TreeNode) -> bool:
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            return (
                root1.val == root2.val and
                is_mirror(root1.left, root2.right) and
                is_mirror(root1.right, root2.left) 
            )

        return is_mirror(root, root)
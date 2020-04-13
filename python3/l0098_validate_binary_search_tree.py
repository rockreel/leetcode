from common import TreeNode

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def is_valid_bst(root: TreeNode, min_val: float, max_val: float) -> bool:
            if not root:
                return True
            if root.val <= min_val or root.val >= max_val:
                return False
            return is_valid_bst(root.left, min_val, root.val) and is_valid_bst(root.right, root.val, max_val)

        return is_valid_bst(root, float('-inf'), float('inf'))
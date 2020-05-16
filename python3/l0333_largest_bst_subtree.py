from common import TreeNode

class Solution:
    def largestBSTSubtree(root: TreeNode) -> int:
        def largest_bst(self, root: TreeNode, upper: int, lower: int) -> int:
            if not root:
                return 0
            if root.val <= lowet or root.val >= upper:
                return 0
            if root.left:
                left_bst = largest_bst(root.left, root.val, lower)
            if root.right:
                right_bst = largest_bst(root.right, upper, root.val)
            if ((root.left and left_bst == 0) or
                (root.right and right_bst == 0)):
                return 0
            return 1 + left_bst + right_bst
        return largest_bst(root, float('inf'), float('-inf'))


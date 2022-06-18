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

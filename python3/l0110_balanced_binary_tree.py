from common import TreeNode
from typing import Tuple

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def is_balanced_and_depth(root: TreeNode) -> Tuple[bool, int]:
            if not root:
                return (True, 0)
            
            left_balanced, left_depth = is_balanced_and_depth(root.left)
            right_balanced, right_depth = is_balanced_and_depth(root.right)
            return (
                left_balanced and right_balanced and abs(left_depth - right_depth) <= 1,
                1 + max(left_depth, right_depth)
            )

        return is_balanced_and_depth(root)[0]

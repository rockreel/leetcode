from common import TreeNode
from typing import Tuple

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def max_min_depth(root: TreeNode) -> Tuple[int, int]:
            if not root:
                return (0, 0)
            
            left_max, left_min = max_min_depth(root.left)
            right_max, right_min = max_min_depth(root.right)
            return 1 + max(left_max, right_max), 1 + min(left_min, right_min)

        max_depth, min_depth = max_min_depth(root)
        return max_depth - min_depth <= 1

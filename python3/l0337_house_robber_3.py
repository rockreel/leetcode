from common import TreeNode
from typing import Tuple

class Solution:
    def rob(self, root: TreeNode) -> int:
        def max_rob(root: TreeNode) -> Tuple[int, int]:
            # Return max money and max money from children.
            if not root:
                return 0, 0
            if not root.left and not root.right:
                return root.val, 0
            l_max, l_sub_max = max_rob(root.left)
            r_max, r_sub_max = max_rob(root.right)
            
            max_ = max(root.val + l_sub_max + r_sub_max, l_max + r_max)
            return max_, l_max + r_max
        return max_rob(root)[0]

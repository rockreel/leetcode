from common import TreeNode
from typing import List

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        view_left = self.rightSideView(root.left)
        view_right = self.rightSideView(root.right)
        return [root.val] + view_right + view_left[len(view_right):]

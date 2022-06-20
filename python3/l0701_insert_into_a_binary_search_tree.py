from common import TreeNode
from typing import Optional

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        curr = root
        while curr:
            if curr.val > val:
                if not curr.left:
                    curr.left = TreeNode(val)
                    break
                else:
                    curr = curr.left
            else:
                if not curr.right:
                    curr.right = TreeNode(val)
                    break
                else:
                    curr = curr.right
        return root
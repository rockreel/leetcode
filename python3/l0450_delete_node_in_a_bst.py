from typing import Optional
from common import TreeNode

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val == key:
            if not root.left and not root.right:
                return None
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # Find minimum value on root.right and set root value to it.
            curr = root.right
            min_value = 0
            while curr:
                min_value = curr.val
                curr = curr.left
            root.val = min_value
            root.right = self.deleteNode(root.right, min_value)
            return root
        else:
            if root.val > key:
                root.left = self.deleteNode(root.left, key)
            else:
                root.right = self.deleteNode(root.right, key)
            return root
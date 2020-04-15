from common import TreeNode
import common

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def flatten_and_return_end(root: TreeNode) -> TreeNode:
            if not root:
                return None

            if not root.left and not root.right:
                return root

            if not root.left:
                return flatten_and_return_end(root.right)

            flatten_end = flatten_and_return_end(root.left)
            if root.right:
                flatten_end.right = root.right
                flatten_end = flatten_and_return_end(root.right)
            root.right = root.left
            root.left = None
            
            return flatten_end

        flatten_and_return_end(root)
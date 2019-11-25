# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        def next_right(root, next_root):
            if root is None:
                return
            if root.left:
                root.left.next = root.right
                next_right(root.left, root.right)
            if root.right:
                next_root = next_root.left if next_root else None
                root.right.next = next_root
                next_right(root.right, next_root)
        
        next_right(root, None)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def build_tree(preorder, pre_start, pre_end, inorder, in_start, in_end):
            if pre_start == pre_end:
                return None
            root = TreeNode(preorder[pre_start])
            root_idx = inorder.index(root.val)
            left_tree_size = root_idx - in_start
            # Split inorder array for left and right subtree.
            root.left = build_tree(
                preorder, pre_start+1, pre_start+1+left_tree_size,
                inorder, in_start, in_start+left_tree_size)
            root.right = build_tree(
                preorder, pre_start+1+left_tree_size, pre_end,
                inorder, in_start+left_tree_size+1, in_end)
            return root
            
        return build_tree(preorder, 0, len(preorder), inorder, 0, len(inorder))


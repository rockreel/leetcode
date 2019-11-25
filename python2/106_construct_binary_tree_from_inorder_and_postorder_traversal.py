# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def build_tree(inorder, in_start, in_end,
                       postorder, post_start, post_end):
            if post_start >= post_end:
                return None
                
            root = TreeNode(postorder[post_end-1])
            root_idx = inorder.index(root.val)
            left_tree_size = root_idx - in_start
                   
            root.left = build_tree(
                inorder, in_start, in_start+left_tree_size,
                postorder, post_start, post_start+left_tree_size)
            root.right = build_tree(
                inorder, in_start+left_tree_size+1, in_end,
                postorder, post_start+left_tree_size, post_end-1)
            return root
            
        return build_tree(
            inorder, 0, len(inorder), postorder, 0, len(postorder))


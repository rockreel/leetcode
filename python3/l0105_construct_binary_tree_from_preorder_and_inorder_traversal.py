from common import TreeNode
from typing import List

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        left_tree_size = inorder.index(preorder[0])

        left_preorder = preorder[1:left_tree_size+1]
        right_preorder = preorder[left_tree_size+1:]
        left_inorder = inorder[:left_tree_size]
        right_inorder = inorder[left_tree_size+1:]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        return root
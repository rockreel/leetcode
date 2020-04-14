from common import TreeNode
from typing import List

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder:
            return None
        
        root = TreeNode(postorder[-1])
        left_tree_size = inorder.index(postorder[-1])

        left_postorder = postorder[:left_tree_size]
        right_postorder = postorder[left_tree_size:-1]
        left_inorder = inorder[:left_tree_size]
        right_inorder = inorder[left_tree_size+1:]

        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)
        return root
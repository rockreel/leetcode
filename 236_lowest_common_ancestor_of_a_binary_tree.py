# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def get_ancestors(root, p, q, ancestors):
            # Return a list may contain p, q if found under root.
            if not root:
                return []
            if root == p or root == q:
                nodes = [root]
            else:
                nodes = []
            nodes.extend(get_ancestors(root.left, p, q, ancestors))
            nodes.extend(get_ancestors(root.right, p, q, ancestors))
            if len(nodes) == 2:
                ancestors.append(root)
            return nodes
            
        ancestors = []
        get_ancestors(root, p, q, ancestors)
        return ancestors[0]


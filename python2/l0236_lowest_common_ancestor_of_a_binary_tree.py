# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Two pass to find path from root to p and q.
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def findPath(root, node, path):
            if not root:
                return False
            path.append(root)
            if root == node:
                return True
            if findPath(root.left, node, path) or findPath(root.right, node, path):
                return True
            path.pop()
            return False
        
        from itertools import izip_longest
        path1 = []
        path2 = []
        findPath(root, p, path1)
        findPath(root, q, path2)
        
        prev_node = None
        for n1, n2 in izip_longest(path1, path2):
            if n1 != n2:
                return prev_node
            prev_node = n1
        return None


# One pass recursive method.
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
            
        if root == p or root == q:
            return root
            
        lca = self.lowestCommonAncestor(root.left, p, q)
        rca = self.lowestCommonAncestor(root.right, p, q)
        
        if lca and rca:
            return root
        elif lca:
            return lca
        else:
            return rca


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


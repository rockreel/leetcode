# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue = [root, None]
        nodes = []
        while queue[0] is not None:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
            if queue[0] is None:
                nodes.append(node.val)
                queue.append(None)
                queue.pop(0)
            
        return nodes


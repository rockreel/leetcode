# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def findWrongNodes(root, last_visited, wrong_nodes):
            if not root:
                return last_visited
    
            last_visited = findWrongNodes(root.left, last_visited, wrong_nodes)
            if last_visited and root.val < last_visited.val:
                wrong_nodes.append((last_visited, root))

            last_visited = findWrongNodes(root.right, root, wrong_nodes)
            return last_visited
        
        wrong_nodes = []
        findWrongNodes(root, None, wrong_nodes)
        
        if len(wrong_nodes) == 2:
            # Swapped nodes not next to each other. Swap first one's last visit
            # to second one's current nodes.
            tmp = wrong_nodes[0][0].val
            wrong_nodes[0][0].val = wrong_nodes[1][1].val
            wrong_nodes[1][1].val = tmp
        elif len(wrong_nodes) == 1:
            # Swapped nodes next to each other. Swap last visit with current nodes.
            tmp = wrong_nodes[0][0].val
            wrong_nodes[0][0].val = wrong_nodes[0][1].val
            wrong_nodes[0][1].val = tmp
        
        return


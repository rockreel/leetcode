# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def findPath(root, sum, curr_path, paths):
            if not root:
                return
            
            curr_path.append(root.val)
            if root.val == sum and not root.left and not root.right:
                paths.append(curr_path[:])
                curr_path.pop()
                return

            findPath(root.left, sum-root.val, curr_path, paths)
            findPath(root.right, sum-root.val, curr_path, paths)
            curr_path.pop()
            return
            
        
        paths = []
        curr_path = []
        findPath(root, sum, curr_path, paths)
        
        return paths


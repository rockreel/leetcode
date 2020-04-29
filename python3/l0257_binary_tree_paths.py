from common import TreeNode

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        paths = []
        for p in self.binaryTreePaths(root.left):
            paths.append('%s->%s' % (str(root.val), p))
        for p in self.binaryTreePaths(root.right):
            paths.append('%s->%s' % (str(root.val), p))
        return paths
        

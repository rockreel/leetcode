from common import TreeNode

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        l_depth = 0
        p = root
        while p:
            p = p.left
            l_depth += 1
        r_depth = 0
        p = root
        while p:
            p = p.right
            r_depth += 1
        if l_depth == r_depth:
            return 2 ** l_depth - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
            

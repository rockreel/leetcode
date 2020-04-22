from common import TreeNode

class Solution:
    """
    @param root: the root of binary tree
    @return: new root
    """
    def upsideDownBinaryTree(self, root):
        # write your code here
        stack = []
        current = root
        while current:
            stack.append(current)
            if current.left:
                stack.append(current.right)
            temp = current
            current = current.left
            temp.right = None
            temp.left = None
        p = dummy = TreeNode(0)
        while stack:
            p.right = stack.pop()
            if stack:
                p.right.left = stack.pop()
            p = p.right
        
        return dummy.right

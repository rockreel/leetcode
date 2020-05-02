class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        if not root or not p:
            return None

        if p.right:
            n = p.right
            while n.left:
                n = n.left
            return n
 
        n = root
        s = None
        while n != p:
            if p.val > n.val:
                n = n.right
            else:
                s = n
                n = n.left
        return s


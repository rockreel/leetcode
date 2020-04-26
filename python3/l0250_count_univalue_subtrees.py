class Solution:
    """
    @param root: the given tree
    @return: the number of uni-value subtrees.
    """
    def countUnivalSubtrees(self, root):
        # write your code here
        
        def unival_tree(root):
            if not root:
                return None, 0
            if not root.left and not root.right:
                return root.val, 1
            
            l_val, l_num = unival_tree(root.left)
            r_val, r_num = unival_tree(root.right)
            
            if root.left is None:
                if root.val == r_val:
                    return root.val, r_num + 1 
            elif root.right is None:
                if root.val == l_val:
                    return root.val, l_num + 1 
            else:
                if l_val == r_val == root.val:
                    return root.val, 1 + l_num + r_num
            
            return None, l_num + r_num
                
        _, num = unival_tree(root)
        return num

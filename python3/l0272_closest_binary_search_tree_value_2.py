from common import TreeNode

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):
        # write your code here
        # Find k lower bounds.
        low_close = []  # Closest lower bounds.
        dummy = TreeNode(None)
        dummy.left = root
        lows = [dummy]  # Stack to track every lower bounds encountered.
        while len(low_close) < k + 1 and lows:
            node = lows.pop()
            if node.val is not None:
                low_close.append(node.val)
            if not node.left:
                continue
            p = node.left
            while p:
                if target >= p.val:
                    lows.append(p)
                    p = p.right
                else:
                    p = p.left        

        # Find k upper bounds.
        up_close = []  # Closest upper bounds.
        dummy = TreeNode(None)
        dummy.right = root
        ups = [dummy]  # Stack to track every upper bounds encountered.
        while len(up_close) < k + 1 and ups:
            node = ups.pop()
            if node.val is not None:
                up_close.append(node.val)
            if not node.right:
                continue
            p = node.right
            while p:
                if target <= p.val:
                    ups.append(p)
                    p = p.left
                else:
                    p = p.right        
        
        # Fins k closest from both low_close and up_close.
        close = []
        i_low, i_up, i = 0, 0, 0
        while i < k:
            if i_low >= len(low_close):
                close.append(up_close[i_up])
                i_up += 1
            elif i_up >= len(up_close):
                close.append(low_close[i_low])
                i_low += 1
            else:
                if low_close[i_low] == up_close[i_up]:
                    close.append(low_close[i_low])
                    i_low += 1
                    i_up += 1
                elif target - low_close[i_low] < up_close[i_up] - target:
                    close.append(low_close[i_low])
                    i_low += 1
                else:
                    close.append(up_close[i_up])
                    i_up += 1
            i += 1
        
        return close
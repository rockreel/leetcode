# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
            
        if not head.next:
            return TreeNode(head.val)
            
        if not head.next.next:
            root = TreeNode(head.val)
            root.right = TreeNode(head.next.val)
            return root
            
        # Find the middle and the previous node.
        dummy = TreeNode(None)
        dummy.next = head
        p0, p1, p2 = None, dummy, dummy
        while p2 and p2.next:
            p0 = p1
            p1 = p1.next
            p2 = p2.next.next
        p0.next = None  # Break the list.
        
        root = TreeNode(p1.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(p1.next)
        
        return root

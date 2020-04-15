from common import ListNode
from common import TreeNode

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        
        if not head.next:
            return TreeNode(head.val)

        if not head.next.next:
            root = TreeNode(head.next.val)
            root.left = TreeNode(head.val)
            return root

        # p1 is the one before the middle node.
        p1, p2 = head, head.next.next
        while p2 and p2.next:
            p2 = p2.next.next
            p1 = p1.next

        root = TreeNode(p1.next.val)
        root.right = self.sortedListToBST(p1.next.next)
        p1.next = None
        root.left = self.sortedListToBST(head)
        return root
from common import ListNode

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        p = head
        while p:
            stack.append(p)
            p = p.next
        p = head
        num_to_link = len(stack) // 2
        i = 0
        while i < num_to_link:
            node = stack.pop()
            node.next = p.next
            p.next = node
            p = node.next
            i += 1
        if p:
            p.next = None
        return
from common import ListNode

class Solution:
    def reorderListStack(self, head: ListNode) -> None:
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

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find second part starting point.
        if not head or not head.next:
            return head
        
        fast, slow, prev = head, head, None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        
        prev.next = None    
        
        # Reverse the second part.
        prev = None 
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # Link together.
        p1 = head
        p2 = prev
        dummy = ListNode(0)
        p = dummy
        while p1 and p2:
            p.next = p1
            p1 = p1.next
            p = p.next
            p.next = p2
            p2 = p2.next
            p = p.next
        p.next = p1 if p1 else p2

        return dummy.next
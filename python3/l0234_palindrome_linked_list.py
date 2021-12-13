from common import ListNode
from typing import Optional

class Solution:

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode(0)
            p = head
            while p:
                n = p.next
                p.next = dummy.next
                dummy.next = p
                p = n
            return dummy.next

        # Find middle point.
        dummy = ListNode(0)
        dummy.next = head
        p1, p2 = dummy, dummy
        while p2 and p2.next:
            p2 = p2.next.next
            p1 = p1.next
        # Start of 2nd half.
        head2 = p1.next
        end1 = p1

        # Reverse 2nd half.
        head2 = reverseList(head2)

        # Compare 1st and 2nd half one by one.
        p1, p2 = head, head2
        is_palindrome = True
        while p2:
            if p1.val != p2.val:
                is_palindrome = False
            p1 = p1.next
            p2 = p2.next

        # Reverse 2nd half back (optional).
        head2 = reverseList(head2)
        end1.next = head2

        return is_palindrome

    def isPalindrome2(self, head: ListNode) -> bool:
        values = []
        p = head
        while p:
            values.append(p.val)
            p = p.next
        i, j = 0, len(values) - 1
        while i < j:
            if values[i] != values[j]:
                return False
            i += 1
            j -= 1
        return True

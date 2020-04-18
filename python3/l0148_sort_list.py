from common import ListNode
from typing import Tuple

class Solution:
    def sortList(self, head: ListNode) -> ListNode:

        def merge_sort(head: ListNode, length: int) -> Tuple[ListNode, ListNode]:
            # Sort list for given length, return sorted list and list after length.
            if not head:
                return (None, None)

            if length == 1:
                next_head = head.next
                head.next = None
                return (head, next_head)
            
            new_head_1, next_to_sort_1 = merge_sort(head, length // 2)
            new_head_2, next_to_sort_2 = merge_sort(next_to_sort_1, length // 2 + length % 2)

            # Merge new_head_1 and new_head_2.
            p = dummy = ListNode(0)
            p1, p2 = new_head_1, new_head_2
            while p1 or p2:
                v1 = p1.val if p1 else float('inf')
                v2 = p2.val if p2 else float('inf')
                if v1 <= v2:
                    p.next = p1
                    p1 = p1.next
                else:
                    p.next = p2
                    p2 = p2.next
                p = p.next
            return (dummy.next, next_to_sort_2)
        
        p = head
        length = 0
        while p:
            length += 1
            p = p.next
        return merge_sort(head, length)[0]
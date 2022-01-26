from common import ListNode
from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        f = head
        b = None
        while f:
            next_f = f.next
            next_b = f
            f.next = b
            f = next_f
            b = next_b
        return b
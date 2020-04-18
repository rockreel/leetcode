from common import ListNode

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p_a, len_a = headA, 0
        while p_a and p_a.next:
            len_a += 1
            p_a = p_a.next
        p_b, len_b = headB, 0
        while p_b and p_b.next:
            len_b += 1
            p_b = p_b.next
        if p_a != p_b:
            return None
        p_a, p_b = headA, headB
        if len_a < len_b:
            p_a, p_b = p_b, p_a
        diff = abs(len_a - len_b)
        while diff > 0:
            p_a =p_a.next
            diff -= 1
        while p_a != p_b:
            p_a =p_a.next
            p_b =p_b.next
        return p_a

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(None)
        r, h1, h2 = head, l1, l2
        carry = 0
        while h1 or h2 or carry:
            v1 = h1.val if h1 else 0
            v2 = h2.val if h2 else 0
            v = v1 + v2 + carry
            carry = v // 10
            r.next = ListNode(v % 10)
            r = r.next
            h1 = h1.next if h1 else None
            h2 = h2.next if h2 else None
        
        return head.next

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def is_palindrome(head, n):
            # Return if linked list with first n node is a palindrome,
            # and also the (n+1)th node.
            if n == 0:
                return True, head
            if n == 1:
                return True, head.next
            if n == 2:
                return head.val == head.next.val, head.next.next
                
            palindrome, next = is_palindrome(head.next, n-2)
            return palindrome and next.val == head.val, next.next

        p, n = head, 0
        while p:
            n += 1
            p = p.next
        
        return is_palindrome(head, n)[0]


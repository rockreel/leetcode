from common import ListNode

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
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

import unittest

from l0708_insert_into_a_sorted_circular_linked_list import ListNode, Solution

class Test(unittest.TestCase):
    
    def validate_list(self, expected_values, node):
        p = node
        i = 0
        while p:
            self.assertEqual(expected_values[i], p.val)
            p = p.next
            i += 1
            if p == node:
                break

    def test_solution(self):
        # Test case 1.
        n1 = ListNode(3)
        n2 = ListNode(5)
        n3 = ListNode(1)
        n1.next = n2
        n2.next = n3
        n3.next = n1
        r = Solution().insert(n1, 4)
        self.validate_list([4, 5, 1, 3], r)

        # Test case 2.
        n1 = ListNode(2)
        n2 = ListNode(2)
        n3 = ListNode(2)
        n1.next = n2
        n2.next = n3
        n3.next = n1
        r = Solution().insert(n1, 3)
        self.validate_list([3, 2, 2, 2], r)

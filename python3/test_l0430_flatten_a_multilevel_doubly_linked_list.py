import unittest

from l0430_flatten_a_multilevel_doubly_linked_list import Node, Solution

class Test(unittest.TestCase):

    def validate_list(self, expected_values, head):
        i = 0
        p = head
        tail = None
        self.assertIsNone(head.prev)
        while p:
            self.assertIsNone(p.child)
            self.assertEqual(expected_values[i], p.val)
            i += 1
            tail = p # Record the tail for latter use.
            p = p.next
        i = 1
        p = tail
        self.assertIsNone(tail.next)
        while p:
            self.assertEqual(expected_values[-i], p.val)
            i += 1
            p = p.prev
        
    
    def test_solution(self):
        # Test case 1.
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        n5 = Node(5)
        n6 = Node(6)
        n7 = Node(7)
        n8 = Node(8)
        n9 = Node(9)
        n10 = Node(10)
        n11 = Node(11)
        n12 = Node(12)
        n1.next = n2
        n2.prev = n1
        n2.next = n3
        n3.prev = n2
        n3.next = n4
        n4.prev = n3
        n4.next = n5
        n5.prev = n4
        n5.next = n6
        n6.prev = n5
        n3.child = n7
        n7.next = n8
        n8.prev = n7
        n8.next = n9
        n9.prev = n8
        n9.next = n10
        n10.prev = n9
        n8.child = n11
        n11.next = n12
        n12.prev = n11
        head = Solution().flatten(n1)
        self.validate_list([1, 2, 3, 7, 8, 11, 12, 9, 10, 4, 5, 6], head)

        # Test case 2.
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n1.next = n2
        n2.prev = n1
        n1.child = n3
        head = Solution().flatten(n1)
        self.validate_list([1, 3, 2], head)

        # Test case 3.
        head = Solution().flatten(None)
        self.assertIsNone(head)

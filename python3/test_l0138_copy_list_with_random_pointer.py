import unittest

from l0138_copy_list_with_random_pointer import Node
from l0138_copy_list_with_random_pointer import Solution

class Test(unittest.TestCase):
    
    def validate_list(self, list1: Node, list2: Node):
        node_map = {}
        p1, p2 = list1, list2
        while p1 and p2:
            self.assertEqual(p1.val, p2.val)
            node_map[p1] = p2
            p1 = p1.next
            p2 = p2.next
        self.assertIsNone(p1)
        self.assertIsNone(p2)
        p1, p2 = list1, list2
        while p1 and p2:
            if p1.random:
                self.assertEqual(node_map[p1.random], p2.random)
            p1 = p1.next
            p2 = p2.next

    def test_solution(self):
        # Test case 1.
        n1 = Node(7)
        n2 = Node(13)
        n3 = Node(11)
        n4 = Node(10)
        n5 = Node(1)
        n1.next = n2
        n2.next = n3
        n3.next = n4
        n4.next = n5
        n2.random = n1
        n3.random = n5
        n4.random = n3
        n5.random = n1
        cloned = Solution().copyRandomList(n1)
        self.validate_list(n1, cloned)

        # Test case 2.
        n1 = Node(1)
        n2 = Node(2)
        n1.next = n2
        n1.random = n2
        n2.random = n2
        cloned = Solution().copyRandomList(n1)
        self.validate_list(n1, cloned)

        # Test case 3.
        n1 = Node(3)
        n2 = Node(3)
        n3 = Node(3)
        n1.next = n2
        n2.next = n3
        n2.random = n1
        cloned = Solution().copyRandomList(n1)
        self.validate_list(n1, cloned)

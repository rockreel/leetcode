import unittest

from l0138_copy_list_with_random_pointer import Node
from l0138_copy_list_with_random_pointer import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        head = Node(1)
        cloned = Solution().copyRandomList(head)
        self.assertEqual(head.val, cloned.val)

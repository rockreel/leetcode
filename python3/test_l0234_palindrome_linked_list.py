import unittest

import common
from l0234_palindrome_linked_list import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            False,
            Solution().isPalindrome(common.create_linked_list([1, 2]))
        )
        self.assertEqual(
            True,
            Solution().isPalindrome(common.create_linked_list([1, 2, 2, 1]))
        )

import unittest

from common import create_binary_tree

from l0501_find_mode_in_binary_search_tree import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual([2], Solution().findMode(create_binary_tree([1,None,2,2])))
        self.assertEqual([0], Solution().findMode(create_binary_tree([0])))
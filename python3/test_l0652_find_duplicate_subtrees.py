import unittest
import common

from l0652_find_duplicate_subtrees import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            sorted([[2, 4], [4]]),
            sorted([common.convert_binary_tree_to_list(n) 
             for n in Solution().findDuplicateSubtrees(
                 common.create_binary_tree([1, 2, 3, 4, None, 2, 4, None, None, 4]))]))
        self.assertEqual(
            sorted([[1]]),
            sorted([common.convert_binary_tree_to_list(n) 
             for n in Solution().findDuplicateSubtrees(
                 common.create_binary_tree([2, 1, 1]))]))
        self.assertEqual(
            sorted([[2, 3], [3]]),
            sorted([common.convert_binary_tree_to_list(n) 
             for n in Solution().findDuplicateSubtrees(
                 common.create_binary_tree([2, 2, 2, 3, None, 3, None]))]))

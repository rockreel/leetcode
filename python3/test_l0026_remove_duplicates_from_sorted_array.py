import unittest

from l0026_remove_duplicate_from_sorted_array import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        list1 = [1, 1, 2]
        self.assertEqual([1, 2], list1[:Solution().removeDuplicates(list1)])
        list2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        self.assertEqual([0, 1, 2, 3, 4], list2[:Solution().removeDuplicates(list2)])
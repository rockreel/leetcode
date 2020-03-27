import unittest

from l0027_remove_element import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        list1 = [3, 2, 2, 3]
        self.assertEqual([2, 2], list1[:Solution().removeElement(list1, 3)])
        list2 = [0, 1, 2, 2, 3, 0, 4, 2]
        self.assertEqual([0, 1, 3, 0, 4], list2[:Solution().removeElement(list2, 2)])
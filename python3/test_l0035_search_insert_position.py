import unittest

from l0035_search_insert_position import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(2, Solution().searchInsert([1, 3, 5, 6], 5))
        self.assertEqual(1, Solution().searchInsert([1, 3, 5, 6], 2))
        self.assertEqual(4, Solution().searchInsert([1, 3, 5, 6], 7))
        self.assertEqual(0, Solution().searchInsert([1, 3, 5, 6], 0))


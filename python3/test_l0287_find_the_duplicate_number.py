import unittest

from l0287_find_duplicate_number import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(2, Solution().findDuplicate([1, 3, 4, 2, 2]))
        self.assertEqual(3, Solution().findDuplicate([3, 1, 3, 4, 2]))
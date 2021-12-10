import unittest

from l0448_find_all_numbers_disappeared_in_an_array import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            [5, 6], 
            Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
        self.assertEqual(
            [2], 
            Solution().findDisappearedNumbers([1, 1]))

        
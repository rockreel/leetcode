import unittest

from l0080_remove_duplicates_from_sorted_array_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        nums = [1, 1, 1, 2, 2, 3]
        self.assertEqual(5, Solution().removeDuplicates(nums))
        self.assertEqual([1, 1, 2, 2, 3], nums[:5])

        nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
        self.assertEqual(7, Solution().removeDuplicates(nums))
        self.assertEqual([0, 0, 1, 1, 2, 3, 3], nums[:7])

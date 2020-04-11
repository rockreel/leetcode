import unittest

from l0075_sort_colors import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        nums = [2, 0, 2, 1, 1, 0]
        Solution().sortColors(nums)
        self.assertEqual([0, 0, 1, 1, 2, 2], nums)

        nums = [1, 2, 0]
        Solution().sortColors(nums)
        self.assertEqual([0, 1, 2], nums)

        nums = [1, 0]
        Solution().sortColors(nums)
        self.assertEqual([0, 1], nums)
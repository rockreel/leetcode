import unittest

from l0031_next_permutation import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        nums = [1, 2, 3]
        Solution().nextPermutation(nums)
        self.assertEqual([1, 3, 2], nums)

        nums = [3, 2, 1]
        Solution().nextPermutation(nums)
        self.assertEqual([1, 2, 3], nums)

        nums = [1, 1, 5]
        Solution().nextPermutation(nums)
        self.assertEqual([1, 5, 1], nums)

        nums = [1, 5, 1]
        Solution().nextPermutation(nums)
        self.assertEqual([5, 1, 1], nums)

import unittest

from l1089_duplicate_zeros import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        arr = [1, 0, 2, 3, 0, 4, 5, 0]
        Solution().duplicateZeros(arr)
        self.assertEqual([1, 0, 0, 2, 3, 0, 0, 4], arr)

        arr = [1, 2, 3]
        Solution().duplicateZeros(arr)
        self.assertEqual([1, 2, 3], arr)

        arr = [0, 0, 0, 0, 0, 0, 0]
        Solution().duplicateZeros(arr)
        self.assertEqual([0, 0, 0, 0, 0, 0, 0], arr)

        
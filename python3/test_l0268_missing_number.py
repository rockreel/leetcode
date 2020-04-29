import unittest

from l0268_missing_number import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(2, Solution().missingNumber([3, 0, 1]))
        self.assertEqual(8, Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))

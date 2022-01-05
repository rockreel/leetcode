import unittest

from l0410_split_array_largest_sum import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            18, 
            Solution().splitArray([7, 2, 5, 10, 8], 2))
        self.assertEqual(
            9, 
            Solution().splitArray([1, 2, 3, 4, 5], 2))
        self.assertEqual(
            4, 
            Solution().splitArray([1, 4, 4], 3))

        